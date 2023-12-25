<template>
  <div>
    <form class="contact-form" @change="changeSelectedGraph">
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
  name: "AnalysisForm",
  data() {
    return {
      Graphs: ["Box Plot","Histogram", "Scatter Plot"],
      selectedGraph: "Box Plot",
    };
  },
  methods: {
    ...mapActions("meta", ["changeGraphs"]),
    changeSelectedGraph() {
      event.preventDefault();
      const payload = {
        graph: this.selectedGraph,
      };
      this.changeGraphs({ payload });
    },
  },
};
</script>

<style scoped>
.form-group {
  display: flex;
  flex-direction: column;
  align-items: center;
}

</style>

