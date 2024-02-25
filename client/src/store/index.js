import Vue from 'vue'
import Vuex from 'vuex'
import common from './modules/common';
import meta from './modules/meta';
import csv from './modules/csv';

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    meta,
    csv, 
    common,
  },
});
