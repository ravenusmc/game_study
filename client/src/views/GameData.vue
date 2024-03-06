<template>
  <div>
    <div>
      <div class="title-div">
        <h2 class="center">Game Data Analysis</h2>
      </div>
      <div>
        <GameDataForm />
      </div>
      <div>
        <BlankData v-if="!dataReceived" />
        <Results v-if="dataReceived" />
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import GameDataForm from "@/components/gamedata/GameDataForm.vue";
import BlankData from "@/components/gamedata/BlankData.vue";
import Results from "@/components/gamedata/Results.vue";

export default {
  name: "GameData",
  components: {
    GameDataForm,
    BlankData,
    Results,
  },
  computed: {
    ...mapGetters("csv", ["dataReceived"]),
  },
};
</script>

<style scoped>

.title-div {
  margin-top: 50px;
	text-transform: uppercase;
}
</style>