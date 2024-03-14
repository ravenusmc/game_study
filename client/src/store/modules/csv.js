import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import store from '@/store/index';

Vue.use(Vuex);

const data = {
	dataReceived: false, 
	selectedYear: 0,
	selectedGenre: "",
	bestSingleGameByYear: "",
	bestSingleGameByYearScore: 0,
	bestGameByGenreAndYear: [],
	topFiveGamesAndScoresSelectedYear: [],
	topPublishersBySelectedYear: [],
	topPublishersBySelectedYearAndGenre: [],
	yearAndCriticRatings: [],
	topFiveGraph: true,
	topPublishersGraph: false,
	topPublishersBySelectedYearAndGenreGraph: false,
};

const getters = {
	dataReceived: (state) => state.dataReceived,
	selectedYear: (state) => state.selectedYear,
	selectedGenre: (state) => state.selectedGenre,
	bestSingleGameByYear: (state) => state.bestSingleGameByYear,
	bestSingleGameByYearScore: (state) => state.bestSingleGameByYearScore,
	bestGameByGenreAndYear: (state) => state.bestGameByGenreAndYear,
	topFiveGamesAndScoresSelectedYear: (state) => state.topFiveGamesAndScoresSelectedYear,
	topPublishersBySelectedYear: (state) => state.topPublishersBySelectedYear,
	topPublishersBySelectedYearAndGenre: (state) => state.topPublishersBySelectedYearAndGenre,
	yearAndCriticRatings: (state) => state.yearAndCriticRatings,
	topFiveGraph: (state) => state.topFiveGraph, 
	topPublishersGraph: (state) => state.topPublishersGraph,
	topPublishersBySelectedYearAndGenreGraph: (state) => state.topPublishersBySelectedYearAndGenreGraph,
};


const actions = {

	submitSelectionToServer: ({ commit }, { payload }) => {
		commit('setSelectedYear', payload['year'])
		commit('setSelectedGenre', payload['genre'])
		const path = 'http://localhost:5000/buildCSVCharts';
		axios.post(path, payload)
			.then((res) => {
				console.log(res.data)
				commit('setDataReceived', true)
				commit('setBestSingleGameByYear', res.data['best_single_game'])
				commit('setBestSingleGameByYearScore', res.data['best_game_score'])
				commit('setBestGameByGenreAndYear', res.data['best_game_by_genre_and_year'])
				commit('setTopFiveGamesAndScoresSelectedYear', res.data['top_five_games_and_scores_selected_year'])
				commit('setTopPublishersBySelectedYear', res.data['top_publishers_by_selected_year'])
				console.log(res.data['top_publishers_by_selected_year_and_genre'])
				commit('setTopPublishersBySelectedYearAndGenre', res.data['top_publishers_by_selected_year_and_genre'])
				res.data['year_and_critic_ratings'] = res.data['year_and_critic_ratings'].map(([year, rating]) => [
					new Date(year, 0, 1),
					rating,
				]);
				commit('setYearAndCriticRatings', res.data['year_and_critic_ratings'])
			})
			.catch((error) => {
				console.log(error);
			});
	},

	submitGenreSelectionToServer: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/buildGenreGraph';
		axios.post(path, payload)
		.then((res) => {
			res.data = res.data.map((innerArray) => {
				return innerArray.map((value, index) => (index === 0 ? new Date(value, 0, 1) : value));
			});
			commit('setYearAndCriticRatings', res.data)
		})
		.catch((error) => {
			console.log(error);
		});
	},

	changeDataGraphs: ({ commit }, { payload }) => {
		const graphType = payload['graph'];
		commit('setTopFiveGraph', graphType === "Top 5 Games for Selected Year");
		commit('setTopPublishers', graphType === "Top Publishers in Selected Year");
		commit('setTopPublishersBySelectedYearAndGenreGraph', graphType === "Top Publishers in Selected Year and Genre")
		// commit('setShowScatterPlotGraph', graphType !== "Box Plot" && graphType !== "Histogram");
	},

};

const mutations = {

	setDataReceived(state, value) {
		state.dataReceived = value; 
	},

	setSelectedYear(state, value) {
		state.selectedYear = value
	},

	setSelectedGenre(state, value) {
		state.selectedGenre = value
	},

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

	setTopPublishersBySelectedYearAndGenre(state, value) {
		state.topPublishersBySelectedYearAndGenre = value
	},

	setTopPublishersBySelectedYear(state, value) {
		state.topPublishersBySelectedYear = value
	},

	setYearAndCriticRatings(state, value) {
		state.yearAndCriticRatings = value
	},

	setTopFiveGraph(state, value) {
		state.topFiveGraph = value
	},

	setTopPublishers(state, value) {
		state.topPublishersGraph = value
	},

	setTopPublishersBySelectedYearAndGenreGraph(state, value) {
		state.topPublishersBySelectedYearAndGenreGraph = value
	},

};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};