<template>
  <div>
    <h1>{{bestSingleGameByYear}}</h1>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "Results",
  computed: {
    ...mapGetters("csv", [
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