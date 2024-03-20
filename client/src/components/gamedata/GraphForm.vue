<template>
  <div>
    <form class="contact-form" @change="changeGraph">
      <div class="form-group">
        <label for="party">Select Graph:</label>
        <select v-model="selectedGraph">
          <option disabled value="">Please select one</option>
          <option v-for="graphOption in graphOptions" :key="graphOption" :value="graphOption">
            {{ graphOption }}
          </option>
        </select>
      </div>
    </form>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "GraphForm",
    computed: {
    ...mapGetters("csv", [
      "graphOptions"
    ]),
  },
  data() {
    return {
      Graphs: ["Top 5 Games for Selected Year", "Top Publishers in Selected Year", "Top Publishers in Selected Year and Genre"],
      selectedGraph: "Top 5 Games for Selected Year",
    };
  },
  methods: {
    ...mapActions("csv", ["changeDataGraphs"]),
    changeGraph() {
      event.preventDefault();
      const payload = {
        graph: this.selectedGraph,
      };
      this.changeDataGraphs({ payload });
    },
  },
};
</script>

<style>
</style>