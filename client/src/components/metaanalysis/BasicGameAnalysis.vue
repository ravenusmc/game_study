<template>
<div>
	<div>
		<h2 class='center'>{{ GameTitle }}</h2>
	</div>
	<div class='basic-data-div'>
		<p>The Critic score is: <span>{{ criticScore }}</span></p>
		<p>The User score is: <span>{{ reviewScore }}</span></p>
	</div>
	<section class='basic-data-section'>
		<CriticData/>
		<UserData/>
	</section>
	<section class='range-graph-section'>
			<BoxPlotGraph :items="allCriticData" />		
			<UserBoxPlotGraph :items="allUserData" />
	</section>
			<!-- <BoxPlotGraph :items="allUserData" />		 -->
</div>
</template>

<script>
import { mapGetters } from "vuex";

import CriticData from "@/components/metaanalysis/CriticData.vue";
import UserData from "@/components/metaanalysis/UserData.vue";
import BoxPlotGraph from "@/components/metaanalysis/BoxPlotGraph.vue";
import UserBoxPlotGraph from "@/components/metaanalysis/UserBoxPlotGraph.vue";

export default {
	name: 'BasicGameAnalysis',
	components: {
		CriticData,
		UserData,
		BoxPlotGraph,
		UserBoxPlotGraph,
	},
	data() {
    return {
      criticData: [],
    };
  },
	computed: {
		...mapGetters("meta", 
		["GameTitle", 
		"allCriticData",
		"criticScore",
		"reviewScore",
		"critic_score_median",
		"allUserData"]),
	},
	// methods: {
	// 	setAllCriticData() {
	// 		console.log('here')
	// 		this.criticData = this.allCriticData
	// 	}
	// },
	// watch: {
	// 	allCriticData: {
	// 		handler(value) {
	// 			if (value) {
	// 				this.setAllCriticData()
	// 			}
	// 		}
	// 	}
	// }
}

</script>

<style scoped>

.basic-data-div {
	display: flex;
	flex-direction: row;
	align-items: center;
	justify-content: center;
}

p {
	margin: 15px;
}

span {
	font-weight: bold;
}

.basic-data-section {
	display: grid;
	grid-template-columns: 1fr 1fr;
	justify-items: center;
}

.range-graph-section {
	border: 2px solid blue;
	display: grid;
	grid-template-columns: 1fr 1fr;
	justify-items: center;
}



</style>