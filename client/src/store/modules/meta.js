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
	showBoxPlotGraph: true, 
	showHistogram: false,
	showScatterPlotGraph: false,
	allCriticData: [],
	critic_score_mean: 0,
	critic_score_median: 0, 
	critic_score_mode: 0,
	critic_score_std_dev: 0, 
	critic_score_max_value: 0,
	critic_score_min_value: 0,
	critic_score_length: 0, 
	critic_lower_quartile: 0,
	critic_interquartile_range: 0,
	critic_upper_quartile: 0,
	critic_histogram: 0,
	allUserData: [],
	user_score_mean: 0,
	user_score_median: 0, 
	user_score_mode: 0, 
	user_score_std_dev: 0, 
	user_score_max_value: 0,
	user_score_min_value: 0,
	user_score_length: 0, 
	user_lower_quartile: 0,
	user_interquartile_range: 0,
	user_upper_quartile: 0,
	user_histogram: 0,
};

const getters = {
	NoData: (state) => state.NoData,
	showBoxPlotGraph: (state) => state.showBoxPlotGraph,
	showHistogram: (state) => state.showHistogram,
	showScatterPlotGraph: (state) => state.showScatterPlotGraph,
	GameTitle: (state) => state.GameTitle,
	criticScore: (state) => state.criticScore,
	reviewScore: (state) => state.reviewScore,
	allCriticData: (state) => state.allCriticData,
	critic_score_mean: (state) => state.critic_score_mean,
	critic_score_median: (state) => state.critic_score_median, 
	critic_score_mode: (state) => state.critic_score_mode,
	critic_score_std_dev: (state) => state.critic_score_std_dev,
	critic_score_max_value: (state) => state.critic_score_max_value,
	critic_score_min_value: (state) => state.critic_score_min_value,
	critic_score_length: (state) => state.critic_score_length,
	critic_lower_quartile: (state) => state.critic_lower_quartile,
	critic_interquartile_range: (state) => state.critic_interquartile_range,
	critic_upper_quartile: (state) => state.critic_upper_quartile,
	critic_histogram: (state) => state.critic_histogram,
	allUserData: (state) => state.allUserData,
	user_score_mean: (state) => state.user_score_mean,
	user_score_median: (state) => state.user_score_median, 
	user_score_mode: (state) => state.user_score_mode,
	user_score_std_dev: (state) => state.user_score_std_dev,
	user_score_max_value: (state) => state.user_score_max_value,
	user_score_min_value: (state) => state.user_score_min_value,
	user_score_length: (state) => state.user_score_length,
	user_lower_quartile: (state) => state.user_lower_quartile,
	user_interquartile_range: (state) => state.user_interquartile_range,
	user_upper_quartile: (state) => state.user_upper_quartile,
	user_histogram: (state) => state.user_histogram,
};


const actions = {

	submitGameNameToServer: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/getGameReviews';
		axios.post(path, payload)
			.then((res) => {
				commit('setGameTitle', res.data['game_title']);
				commit('setCriticScore', res.data['scores'][0])
				commit('setReviewScore', res.data['scores'][1])
				commit('setAllCriticData', res.data['stat_dict'])
				commit('setCriticScoreMean', res.data['stat_dict']['Critic_Score_Mean'])
				commit('setCriticScoreMedian', res.data['stat_dict']['median'])
				commit('setCriticScoreMode', res.data['stat_dict']['Critic_Score_Mode'])
				commit('setCriticScoreStdDev', res.data['stat_dict']['standard_deviation'])
				commit('setCriticScoreMaxValue', res.data['stat_dict']['Data_set_Max_Value'])
				commit('setCriticScoreMinValue', res.data['stat_dict']['data_set_min'])
				commit('setCriticScoreLength', res.data['stat_dict']['Data_set_length'])
				commit('setCriticLowerQuartile', res.data['stat_dict']['lower_qualtile'])
				commit('setCriticInterquartileRange', res.data['stat_dict']['interquartile_range'])
				commit('setCriticUpperQuartile', res.data['stat_dict']['upper_qualtile'])
				commit('setCriticHistogram', res.data['stat_dict']['critic_histogram'])
				commit('setAllUserScore', res.data['user_stat_dict'])
				commit('setUserScoreMean', res.data['user_stat_dict']['User_Score_Mean'])
				commit('setUserScoreMedian', res.data['user_stat_dict']['median'])
				commit('setUserScoreMode', res.data['user_stat_dict']['User_Score_Mode'])
				commit('setUserScoreStdDev', res.data['user_stat_dict']['standard_deviation'])
				commit('setUserScoreMaxValue', res.data['user_stat_dict']['Data_set_Max_Value'])
				commit('setUserScoreMinValue', res.data['user_stat_dict']['data_set_min'])
				commit('setUserScoreLength', res.data['user_stat_dict']['Data_set_length'])
				commit('setUserLowerQuartile', res.data['user_stat_dict']['lower_qualtile'])
				commit('setUserInterquartileRange', res.data['user_stat_dict']['interquartile_range'])
				commit('setUserUpperQuartile', res.data['user_stat_dict']['upper_qualtile'])
				commit('setUserHistogram', res.data['user_stat_dict']['user_histogram'])
				commit('setNoData', false)
			})
			.catch((error) => {
				console.log(error);
			});
	},

	changeGraphs: ({ commit }, { payload }) => {
		const graphType = payload['graph'];
		commit('setShowBoxPlotGraph', graphType === "Box Plot");
		commit('setShowHistogram', graphType === "Histogram");
		commit('setShowScatterPlotGraph', graphType !== "Box Plot" && graphType !== "Histogram");
	},

};

const mutations = {

	setNoData(state, value) {
		state.NoData = value;
	},

	setShowBoxPlotGraph(state, value) {
		state.showBoxPlotGraph = value;
	},

	setShowHistogram(state, value) {
		state.showHistogram = value;
	},

	setShowScatterPlotGraph(state, value) {
		state.showScatterPlotGraph = value;
	},

	setGameTitle(state, value) {
		state.GameTitle = value;
	},

	setAllCriticData(state, value) {
		state.allCriticData = value;
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

	setCriticScoreStdDev(state, value) {
		state.critic_score_std_dev = value;
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

	setCriticLowerQuartile(state, value) {
		state.critic_lower_quartile = value;
	},

	setCriticInterquartileRange(state, value) {
		state.critic_interquartile_range = value;
	},

	setCriticUpperQuartile(state, value) {
		state.critic_upper_quartile = value;
	},

	setCriticHistogram(state, value) {
		state.critic_histogram = value;
	},

	setAllUserScore(state, value) {
		state.allUserData = value;
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

	setUserScoreStdDev(state, value) {
		state.user_score_std_dev = value;
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

	setUserLowerQuartile(state, value) {
		state.user_lower_quartile = value;
	},

	setUserInterquartileRange(state, value) {
		state.user_interquartile_range = value;
	},

	setUserUpperQuartile(state, value) {
		state.user_upper_quartile = value;
	},

	setUserHistogram(state, value) {
		state.user_histogram = value;
	},

};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};