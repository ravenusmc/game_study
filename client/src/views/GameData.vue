<template>
  <div>
    <div class="title-div">
      <h3 class="center">Game Data Analysis</h3>
    </div>

		<div>
			<GameDataForm />
		</div>

    <!-- What graphs to make?
		-Sales, by publisher, by year 
			-Need to see top 5 publishers probably 
			-user clicks button to change to next year
			-DONE  
		-Graph of user scores versus critic score for best game 
			-Should I do this? -->
      <p>test</p>
    <p>{{ bestSingleGameByYear }}</p>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import GameDataForm from "@/components/gamedata/GameDataForm.vue";

export default {
  name: "GameData",
  components: {
    GameDataForm,
  },
  	computed: {
		...mapGetters("csv", 
		["bestSingleGameByYear",]),
	},
};
</script>

<style scoped>
.title-div {
  margin-top: 50px;
}
</style>