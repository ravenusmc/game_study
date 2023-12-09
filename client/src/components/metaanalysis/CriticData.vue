<template>
  <div>
    <h3 class="center">Critic Data</h3>
    <div class="arrange-data">
      <p>
        The Mean is: <span>{{ critic_score_mean }}</span>
      </p>
      <p>
        The Median is: <span>{{ critic_score_median }}</span>
      </p>
      <p>
        The Mode is: <span>{{ critic_score_mode }}</span>
      </p>
      <p>
        The Standard Deviation is: <span>{{ critic_score_std_dev }}</span>
      </p>
      <p>
        The number of Scores is: <span>{{ critic_score_length }}</span>
      </p>
      <p>
        The Max is: <span>{{ critic_score_max_value }}</span>
      </p>
      <p>
        The Min is: <span>{{ critic_score_min_value }}</span>
      </p>
      <p>
        The lower Qualtile is: <span>{{ critic_lower_quartile }}</span>
      </p>
      <p>
        The Upper Qualtile is: <span>{{ critic_upper_quartile }}</span>
      </p>
      <p>
        The Interquartile Range is: <span>{{ critic_interquartile_range }}</span>
      </p>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "CriticData",
  computed: {
    ...mapGetters("meta", [
      "critic_score_mean",
      "critic_score_median",
      "critic_score_mode",
      "critic_score_std_dev",
      "critic_score_max_value",
      "critic_score_min_value",
      "critic_score_length",
      "critic_lower_quartile",
      "critic_interquartile_range",
      "critic_upper_quartile",
    ]),
  },
};
</script>

<style scoped>
span {
  font-weight: bold;
}
</style>