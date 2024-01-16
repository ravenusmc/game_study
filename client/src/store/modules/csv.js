import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import store from '@/store/index';

Vue.use(Vuex);

const data = {
	NoData: true,
};

const getters = {
	NoData: (state) => state.NoData,
};


const actions = {

	submitSelectionToServer: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/buildCSVCharts';
		axios.post(path, payload)
			.then((res) => {
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