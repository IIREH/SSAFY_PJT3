<template>
  <div>
    <v-row class="mb-1">
      <v-col class="text-right">
        <v-btn class="mx-2" fab dark large color="cyan" @click="moveWrite()">
          <v-icon dark> mdi-pencil </v-icon>
        </v-btn>
      </v-col>
    </v-row>
    <div class="container">
      <!-- 하위 component인 ListRow에 데이터 전달(props) -->
      <article-list-row
        v-for="article in articles"
        :key="article.id"
        v-bind="article"
      />
    </div>
  </div>
</template>

<script>
import http from "@/util/http-common";
import ArticleListRow from "@/components/articles/child/ArticleListRow";

export default {
  name: "ArticleList",
  components: {
    ArticleListRow,
  },
  data() {
    return {
      articles: [],
    };
  },
  created() {
    http.get(`/articles/lists/`).then(({ data }) => {
      this.articles = data;
    });
  },
  methods: {
    moveWrite() {
      this.$router.push({ name: "ArticleCreate" });
    },
  },
};
</script>

<style scoped>
.container {
  column-width: 350px;
  column-gap: 15px;
}
</style>
