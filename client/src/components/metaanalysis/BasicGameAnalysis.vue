<template>
<div>
	<div>
		<h2 class='center'>{{ GameTitle }}</h2>
	</div>
	<div class='basic-data-div'>
		<p>The Critic score is: <span>{{ criticScore }}</span></p>
		<p>The User score is: <span>{{ reviewScore }}</span></p>
	</div>
	<section>
		<CriticData/>
	</section>
</div>
</template>

<script>
import { mapGetters } from "vuex";

import CriticData from "@/components/metaanalysis/CriticData.vue";

export default {
	name: 'BasicGameAnalysis',
	components: {
    CriticData,
  },
	computed: {
		...mapGetters("meta", 
		["GameTitle", 
		"criticScore",
		"reviewScore"]),
  },
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

</style>