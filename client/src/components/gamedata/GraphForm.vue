<template>
  <div>
    <form class="contact-form" @change="changeGraph">
      <div class="form-group">
        <label for="party">Select Graph:</label>
        <select v-model="selectedGraph">
          <option disabled value="">Please select one</option>
          <option v-for="graph in Graphs" :key="graph" :value="graph">
            {{ graph }}
          </option>
        </select>
      </div>
    </form>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "GraphForm",
  data() {
    return {
      Graphs: ["Top 5 Games for Selected Year", "Top Publishers in Selected Year"],
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