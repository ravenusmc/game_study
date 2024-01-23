import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import store from '@/store/index';

Vue.use(Vuex);

const data = {
	bestSingleGameByYear: "",
	bestSingleGameByYearScore: 0,
	bestGameByGenreAndYear: [],
	topFiveGamesAndScoresSelectedYear: [],
	topPublishersBySelectedYear: [],
	yearAndCriticRatings: []
};

const getters = {
	bestSingleGameByYear: (state) => state.bestSingleGameByYear,
	bestSingleGameByYearScore: (state) => state.bestSingleGameByYearScore,
	bestGameByGenreAndYear: (state) => state.bestGameByGenreAndYear,
	topFiveGamesAndScoresSelectedYear: (state) => state.topFiveGamesAndScoresSelectedYear,
	topPublishersBySelectedYear: (state) => state.topPublishersBySelectedYear,
	yearAndCriticRatings: (state) => state.yearAndCriticRatings,
};


const actions = {

	submitSelectionToServer: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/buildCSVCharts';
		axios.post(path, payload)
			.then((res) => {
				console.log(res.data)
				commit('setBestSingleGameByYear', res.data['best_single_game'])
				commit('setBestSingleGameByYearScore', res.data['best_game_score'])
				commit('setBestGameByGenreAndYear', res.data['best_game_by_genre_and_year'])
				commit('setTopFiveGamesAndScoresSelectedYear', res.data['top_five_games_and_scores_selected_year'])
				commit('setTopPublishersBySelectedYear', res.data['top_publishers_by_selected_year'])
				commit('setYearAndCriticRatings', res.data['year_and_critic_ratings'])
			})
			.catch((error) => {
				console.log(error);
			});
	},

};

const mutations = {

	setBestSingleGameByYear(state, value) {
		state.bestSingleGameByYear = value;
	},

	setBestSingleGameByYearScore(state, value) {
		state.bestSingleGameByYearScore = value
	},

	setBestGameByGenreAndYear(state, value) {
		state.bestGameByGenreAndYear = value
	},

	setTopFiveGamesAndScoresSelectedYear(state, value) {
		state.topFiveGamesAndScoresSelectedYear = value
	},

	setTopPublishersBySelectedYear(state, value) {
		state.topPublishersBySelectedYear = value
	},

	setYearAndCriticRatings(state, value) {
		state.yearAndCriticRatings = value
	},

};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};