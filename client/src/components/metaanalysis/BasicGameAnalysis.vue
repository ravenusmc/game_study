<template>
<div>
	<h2>{{ GameTitle }}</h2>
	<p>The Critic score is: {{ criticScore }}</p>
	<p>The Review score is: {{ reviewScore }}</p>
</div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
	name: 'BasicGameAnalysis',
	computed: {
		...mapGetters("meta", 
		["GameTitle", 
		"criticScore",
		"reviewScore"]),
  },
}

</script>

<style scoped>

</style>