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
	user_score_mean: 0,
	user_score_median: 0, 
	user_score_mode: 0, 
	user_score_max_value: 0,
	user_score_min_value: 0,
	user_score_length: 0, 

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
	critic_score_length: (state) => state.critic_score_length,
	user_score_mean: (state) => state.user_score_mean,
	user_score_median: (state) => state.user_score_median, 
	user_score_mode: (state) => state.user_score_mode,
	user_score_max_value: (state) => state.user_score_max_value,
	user_score_min_value: (state) => state.user_score_min_value,
	user_score_length: (state) => state.user_score_length,
};

// user_stat_dict
// : 
// Data_set_Max_Value
// : 
// 10
// Data_set_length
// : 
// 24
// User_Score_Mean
// : 
// 8.58
// User_Score_Median
// : 
// 9
// User_Score_Mode
// : 
// 10


const actions = {

	submitGameNameToServer: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/getGameReviews';
		axios.post(path, payload)
			.then((res) => {
				console.log(res.data)
				commit('setGameTitle', res.data['game_title']);
				commit('setCriticScore', res.data['scores'][0])
				commit('setReviewScore', res.data['scores'][1])
				commit('setCriticScoreMean', res.data['stat_dict']['Critic_Score_Mean'])
				commit('setCriticScoreMedian', res.data['stat_dict']['Critic_Score_Median'])
				commit('setCriticScoreMode', res.data['stat_dict']['Critic_Score_Mode'])
				commit('setCriticScoreMaxValue', res.data['stat_dict']['Data_set_Max_Value'])
				commit('setCriticScoreMinValue', res.data['stat_dict']['data_set_min'])
				commit('setCriticScoreLength', res.data['stat_dict']['Data_set_length'])
				commit('setUserScoreMean', res.data['user_stat_dict']['User_Score_Mean'])
				commit('setUserScoreMedian', res.data['user_stat_dict']['User_Score_Median'])
				commit('setUserScoreMode', res.data['user_stat_dict']['User_Score_Mode'])
				commit('setUserScoreMaxValue', res.data['user_stat_dict']['Data_set_Max_Value'])
				commit('setUserScoreMinValue', res.data['user_stat_dict']['data_set_min'])
				commit('setUserScoreLength', res.data['user_stat_dict']['Data_set_length'])
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
	},

	setCriticScoreMean(state, value) {
		state.critic_score_mean = value;
	},

	setCriticScoreMedian(state, value) {
		state.critic_score_median = value;
	},

	setCriticScoreMode(state, value) {
		state.critic_score_mode = value;
	},

	setCriticScoreMaxValue(state, value) {
		state.critic_score_max_value = value;
	},

	setCriticScoreMinValue(state, value) {
		state.critic_score_min_value = value;
	},

	setCriticScoreLength(state, value) {
		state.critic_score_length = value;
	},

	setUserScoreMean(state, value) {
		state.user_score_mean = value;
	},

	setUserScoreMedian(state, value) {
		state.user_score_median = value;
	},

	setUserScoreMode(state, value) {
		state.user_score_mode = value;
	},

	setUserScoreMaxValue(state, value) {
		state.user_score_max_value = value;
	},

	setUserScoreMinValue(state, value) {
		state.user_score_min_value = value;
	},

	setUserScoreLength(state, value) {
		state.user_score_length = value;
	},

	 

};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};