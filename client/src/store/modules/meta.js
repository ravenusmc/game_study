import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import store from '@/store/index';

Vue.use(Vuex);

const data = {
	NoData: true,
	GameTitle: '',
	criticScore: 0,
	reviewScore: 0,
	critic_score_mean: 0,
	critic_score_median: 0, 
	critic_score_mode: 0, 
	critic_score_max_value: 0,
	critic_score_min_value: 0,
	critic_score_length: 0, 
};

const getters = {
	NoData: (state) => state.NoData,
	GameTitle: (state) => state.GameTitle,
	criticScore: (state) => state.criticScore,
	reviewScore: (state) => state.reviewScore,
	critic_score_mean: (state) => state.critic_score_mean,
	critic_score_median: (state) => state.critic_score_median, 
	critic_score_mode: (state) => state.critic_score_mode,
	critic_score_max_value: (state) => state.critic_score_max_value,
	critic_score_min_value: (state) => state.critic_score_min_value,
	critic_score_length: (state) => state. critic_score_length
};

const actions = {

	submitGameNameToServer: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/getGameReviews';
		axios.post(path, payload)
			.then((res) => {
				console.log(res.data)
				commit('setGameTitle', res.data['game_title']);
				commit('setCriticScore', res.data['scores'][0])
				commit('setReviewScore', res.data['scores'][1])
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

	setReviewScore(state, value) {
		state.reviewScore = value;
	}

};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};