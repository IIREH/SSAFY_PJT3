from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import User
from .serializers import UserSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def delete(request, user_pk):
    try:
        user = get_object_or_404(User, pk=user_pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        user.delete()
        return Response({'id': '계정이 삭제되었습니다.'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([AllowAny])
def profile(request, user_pk):
    profile = get_object_or_404(User, pk=user_pk)
    serializer = UserSerializer(profile)
    return Response(serializer.data)

# @api_view(['PUT'])
# def profile(request, user_pk):
#     profile = get_object_or_404(User, pk=user_pk)
#
#     serializer = UserSerializer(profile, data=request.data)
#
#     if serializer.is_valid(raise_exception=True):
#         serializer.save(user=request.user)
#         return Response(serializer.data)

@api_view(['POST'])
def my_profile(request):
    user = get_object_or_404(User, pk=request.data.get('user_id'))
    serializer = UserSerializer(user)

    return Response(serializer.data)