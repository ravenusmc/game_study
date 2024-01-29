<template>
  <div>
    <p>Here are the results for {{ selectedYear }} and the genre that was selected was: {{ selectedGenre}}</p>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "Results",
  computed: {
    ...mapGetters("csv", [
      "selectedYear",
      "selectedGenre",
      "bestSingleGameByYear",
      "bestSingleGameByYearScore",
      "bestGameByGenreAndYear",
      "topFiveGamesAndScoresSelectedYear",
      "topPublishersBySelectedYear",
      "yearAndCriticRatings",
    ]),
  },
};
</script>

<style scoped>
</style>