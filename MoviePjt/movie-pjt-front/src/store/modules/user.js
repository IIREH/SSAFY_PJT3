const user = {
  namespaced: true,

  state: {
    // login μνμ¬λΆ
    isLogin: false,
    userInfo: [],
  },
  getters: {},
  mutations: {
    SET_USER_STATE(state, data) {
      state.isLogin = data;
    },
  },
  actions: {},
};

export default user;
