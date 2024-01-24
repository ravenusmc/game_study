<template>
  <div>
    <div class="title-div">
      <h3 class="center">Game Data Analysis</h3>
    </div>
		<div>
			<GameDataForm />
		</div>
		<section>
			<NoData v-if="!dataReceived"  />
			<Results v-if="dataReceived" />
		</section>
    <p>{{ dataReceived }}</p>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import GameDataForm from "@/components/gamedata/GameDataForm.vue";
import NoData from "@/components/gamedata/NoData.vue";

export default {
  name: "GameData",
  components: {
		GameDataForm,
		NoData,
  },
  	computed: {
		...mapGetters("csv", 
		["dataReceived",
		"bestSingleGameByYear",
		"bestSingleGameByYearScore",
		"bestGameByGenreAndYear",
		"topFiveGamesAndScoresSelectedYear",
		"topPublishersBySelectedYear",
		"yearAndCriticRatings"])
	},
};
</script>

<style scoped>
.title-div {
  margin-top: 50px;
}
</style>