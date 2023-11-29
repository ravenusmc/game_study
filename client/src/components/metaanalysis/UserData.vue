<template>
<div>
	<p>User Data</p>
  <p>User:{{user_score_mean}}</p>
</div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "UserData",
	computed: {
		...mapGetters("meta", 
		["user_score_mean", 
    "critic_score_median",
    "critic_score_mode",
    "critic_score_max_value",
    "critic_score_min_value",
    "critic_score_length"]),
  },
};

</script>

<style scoped>

</style>