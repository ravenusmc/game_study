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
	bestSingleGameByYear: (state) => state.best_single_game_by_year,
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

};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};