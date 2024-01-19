import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import store from '@/store/index';

Vue.use(Vuex);

const data = {
	best_single_game_by_year: "",
};

const getters = {
	best_single_game_by_year: (state) => state.best_single_game_by_year,
};


const actions = {

	submitSelectionToServer: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/buildCSVCharts';
		axios.post(path, payload)
			.then((res) => {
				console.log(res.data)
				commit('setNoData', false)
			})
			.catch((error) => {
				console.log(error);
			});
	},


};

const mutations = {

	setNoData(state, value) {
		state.NoData = value;
	},

};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};