import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import store from '@/store/index';

Vue.use(Vuex);

const data = {
	NoData: true,
	GameTitle: '',
	criticScore: 0,
};

const getters = {
	NoData: (state) => state.NoData,
	GameTitle: (state) => state.GameTitle,
	criticScore: (state) => state.criticScore,
};

const actions = {

	submitGameNameToServer: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/getGameReviews';
		axios.post(path, payload)
			.then((res) => {
				console.log(res.data[1][0])
				commit('setGameTitle', res.data[0]);
				commit('setCriticScore', res.data[1][0])
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

	setGameTitle(state, value) {
		state.GameTitle = value;
	},

	setCriticScore(state, value) {
		state.criticScore = value;
	},

};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};