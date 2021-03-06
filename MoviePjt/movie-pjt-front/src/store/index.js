import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";

import user from "./modules/user.js";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    temp: 1,
  },

  modules: {
    user,
  },

  plugins: [createPersistedState()],
});
