import Vue from 'vue';
import Vuex from 'vuex';
// import axios from 'axios';
import store from '@/store/index';

Vue.use(Vuex);

const data = {
	GameName: '',
};

const getters = {
	GameName: (state) => state.GameName,
};

const actions = {

	submitGameNameToServer: ({ commit }, { payload }) => {
		console.log('ACTION!')
		// const path = 'http://localhost:5000/submitSalesDataToDatabase';
		// axios.post(path, payload)
		// 	.then((res) => {
		// 		commit('current_inventory', false);
		// 	})
		// 	.catch((error) => {
		// 		console.log(error);
		// 	});
	},


};

const mutations = {

	setCurrentInventory(state, value) {
		state.currentInventory = value;
	},

};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};