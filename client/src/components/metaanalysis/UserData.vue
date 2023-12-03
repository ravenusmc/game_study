<template>
  <div>
    <h3 class="center">User Data</h3>
    <p>
      The Mean of the data is: <span>{{ user_score_mean }}</span>
    </p>
    <p>
      The Median of the data is: <span>{{ user_score_median }}</span>
    </p>
    <p>
      The Mode of the data is: <span>{{ user_score_mode }}</span>
    </p>
    <p>
      The number of User Scores is: <span>{{ user_score_length }}</span>
    </p>
    <p>
      The Max of the data is: <span>{{ user_score_max_value }}</span>
    </p>
    <p>
      The Min of the data is: <span>{{ user_score_min_value }}</span>
    </p>
    <p>
      The lower Qualtile is: <span>{{ user_lower_quartile }}</span>
    </p>
    <p>
      The Upper Qualtile is: <span>{{ user_upper_quartile }}</span>
    </p>
    <p>
      The Interquartile Range is: <span>{{ user_interquartile_range }}</span>
    </p>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "UserData",
  computed: {
    ...mapGetters("meta", [
      "user_score_mean",
      "user_score_median",
      "user_score_mode",
      "user_score_max_value",
      "user_score_min_value",
      "user_score_length",
      "user_lower_quartile",
      "user_interquartile_range",
      "user_upper_quartile",
    ]),
  },
};
</script>

<style scoped>
span {
  font-weight: bold;
}
</style>