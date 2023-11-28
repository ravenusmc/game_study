<template>
<div>
	<h3>Critic Data</h3>
  <p>The Mean of the data is: <span>{{critic_score_mean}}</span></p>
  <p>The Median of the data is: <span>{{critic_score_median}}</span></p>
  <p>The Mode of the data is: <span>{{critic_score_mode}}</span></p>
  <p>The number of Critic Scores is: <span>{{critic_score_length}}</span></p>
  <p>The Max of the data is: <span>{{critic_score_max_value}}</span></p>
  <p>The Min of the data is: <span>{{critic_score_min_value}}</span></p>
</div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "CriticData",
	computed: {
		...mapGetters("meta", 
		["critic_score_mean", 
    "critic_score_median",
    "critic_score_mode",
    "critic_score_max_value",
    "critic_score_min_value",
    "critic_score_length"]),
  },
};

</script>

<style scoped>

span {
  font-weight: bold;
}

</style>