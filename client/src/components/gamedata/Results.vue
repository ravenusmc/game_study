<template>
  <div>
    <section class="basic-data-area">
      <div>
        <h3 class="center">Basic Information:</h3>
        <div>
          <p>
            Here are the results for <span>{{ selectedYear }}</span> and the
            genre
            <span>{{ selectedGenre }}:</span>
          </p>
          <p>
            The best game in <span>{{ selectedYear }}</span> was
            <span>{{ bestSingleGameByYear }}</span> and it had a critic score
            was <span>{{ bestSingleGameByYearScore }}</span
            >.
          </p>
          <p>
            The best game in <span>{{ selectedYear }}</span
            >, on the selected genre of <span>{{ selectedGenre }}</span
            >, was <span>{{ bestGameByGenreAndYear[0] }}</span> with a critic
            score of <span>{{ bestGameByGenreAndYear[1] }}</span
            >.
          </p>
        </div>
      </div>
    </section>
    <hr />
    <div class="genre-form">
      <GenreForm />
    </div>
    <section class="graph-area">
      <div v-if="topFiveGraph">
        <GraphCard
          :typeOne="typeOne"
          :data="topFiveGamesAndScoresSelectedYear"
          :options="chartOptionsOne"
        ></GraphCard>
      </div>
      <div v-if="topPublishersGraph">
        <GraphCard
          :typeOne="typeOne"
          :data="topPublishersBySelectedYear"
          :options="chartOptionsTwo"
        >
        </GraphCard>
      </div>
      <div v-if="topPublishersBySelectedYearAndGenreGraph">
        <GraphCard
          :typeOne="typeOne"
          :data="topPublishersBySelectedYearAndGenre"
          :options="chartOptionsFour"
        >
        </GraphCard>
      </div>
    </section>

    <hr />
    <GenreGraphForm />
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
import GenreForm from "@/components/gamedata/GraphForm.vue";
import GenreGraphForm from "@/components/gamedata/GenreGraphForm.vue";

export default {
  name: "Results",
  components: {
    GraphCard,
    GenreForm,
    GenreGraphForm,
  },
  computed: {
    ...mapGetters("csv", [
      "selectedYear",
      "selectedGenre",
      "bestSingleGameByYear",
      "bestSingleGameByYearScore",
      "bestGameByGenreAndYear",
      "topFiveGamesAndScoresSelectedYear",
      "topPublishersBySelectedYearAndGenre",
      "topPublishersBySelectedYear",
      "yearAndCriticRatings",
      "topFiveGraph",
      "topPublishersGraph",
      "topPublishersBySelectedYearAndGenreGraph",
    ]),
  },
  data() {
    return {
      typeOne: "BarChart",
      typeTwo: "LineChart",
      chartOptionsOne: {
        title: "Top 5 Games for Selected Year",
        legend: { position: "top" },
        colors: ["#069AEA"],
        height: 500,
        animation: {
          duration: 1000,
          easing: "linear",
        },
        vAxis: {
          title: "Game Title",
          viewWindow: {
            min: 0,
          },
        },
        hAxis: {
          title: "Score",
        },
      },
      chartOptionsTwo: {
        title: "Top Publishers in Selected Year",
        legend: { position: "top" },
        colors: ["#069AEA"],
        height: 500,
        animation: {
          duration: 1000,
          easing: "linear",
        },
        vAxis: {
          title: "Game Publisher",
          viewWindow: {
            min: 0,
          },
        },
        hAxis: {
          title: "Dollars (Millions)",
        },
      },
      chartOptionsThree: {
        title: "Average Scores of Games in Selected Genre(s) Over Time",
        legend: { position: "top" },
        colors: [
          "#069AEA",
          "#EF3C07",
          "#EFA507",
          "#A41D42",
          "#E109DB",
          "#971BF3",
          "#2306F3",
          "#302480",
          "#1D60A7",
          "#189CCD",
          "#09F165",
          "#E5FC00",
        ],
        height: 500,
        vAxis: {
          title: "Average Rating",
          viewWindow: {
            min: 0,
          },
        },
        hAxis: {
          title: "Year",
        },
      },
      chartOptionsFour: {
        title: "Top Publishers in Selected Year and Genre",
        legend: { position: "top" },
        colors: ["#069AEA"],
        height: 500,
        animation: {
          duration: 1000,
          easing: "linear",
        },
        vAxis: {
          title: "Game Publisher",
          viewWindow: {
            min: 0,
          },
        },
        hAxis: {
          title: "Dollars (Millions)",
        },
      },
    };
  },
};
</script>

<style scoped>
span {
  font-weight: bold;
}

.basic-data-area {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin: 15px;
  border: 3px solid red;
}

.genre-form {
  display: flex;
  justify-content: center;
}

.graph-area {
  margin: 50px;
}
</style>