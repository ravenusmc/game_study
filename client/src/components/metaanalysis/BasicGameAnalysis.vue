<template>
<div>
	<h2>{{ GameTitle }}</h2>
	<p>The Critic score is: {{ criticScore }}</p>
</div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
	name: 'BasicGameAnalysis',
	computed: {
    ...mapGetters("meta", ["GameTitle", "criticScore"]),
  },
}

</script>

<style scoped>

</style>