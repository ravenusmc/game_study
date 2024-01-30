<template>
  <div>
    <p>
      Here are the results for {{ selectedYear }} and the genre that was
      selected was: {{ selectedGenre }}
    </p>
    <p>
      The best game that year was {{ bestSingleGameByYear }}. It's critic score
      was {{ bestSingleGameByYearScore }}.
    </p>
    <p>
      The best game that year, on the selected genre, was
      {{ bestGameByGenreAndYear[0] }}. It's critic score was
      {{ bestGameByGenreAndYear[1] }}.
    </p>
    <GraphCard
      :typeOne="typeOne"
      :data="topFiveGamesAndScoresSelectedYear"
      :options="chartOptionsOne"
    >
    </GraphCard>
    <GraphCard
      :typeOne="typeOne"
      :data="topPublishersBySelectedYear"
      :options="chartOptionsTwo"
    >
    </GraphCard>
    <GraphCard
      :typeOne="typeTwo"
      :data="yearAndCriticRatings"
      :options="chartOptionsThree"
    >
    </GraphCard>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import GraphCard from "@/components/graphs/GraphCard.vue";

export default {
  name: "Results",
  components: {
    GraphCard,
  },
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
  data() {
    return {
      typeOne: "BarChart",
      typeTwo: "LineChart",
      chartOptionsOne: {
        title: "Top 5 Games for Selected Year",
        legend: { position: "top" },
        colors: ["#BF0D3E"],
        height: 500,
        animation: {
          duration: 1000,
          easing: "linear",
        },
        vAxis: {
          viewWindow: {
            min: 0,
          },
        },
      },
      chartOptionsTwo: {
        title: "Top Publishers in selected year",
        legend: { position: "top" },
        colors: ["#BF0D3E"],
        height: 500,
        vAxis: {
          viewWindow: {
            min: 0,
          },
        },
      },
      chartOptionsThree: {
        title: "Average Scores of Games in Selected Genre Over Time",
        legend: { position: "top" },
        colors: ["#BF0D3E"],
        height: 500,
        vAxis: {
          viewWindow: {
            min: 0,
          },
        },
      },
    };
  },
};
</script>

<style scoped>
</style>