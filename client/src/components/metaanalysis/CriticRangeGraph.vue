<template>
  <div>
    <p>{{ items }}</p>
    <p>{{ min }}</p>
    <div id="my_dataviz"></div>
  </div>
</template>

<script>
import * as d3 from "d3";

export default {
  data() {
    // Assign the prop to a data element for modification
    return {
      median: this.items["Critic_Score_Median"],
			min: this.items["data_set_min"],
			q1: this.items["lower_qualtile"]
    };
  },
  props: {
    items: {
      type: Array,
      required: true,
    },
  },
  methods: {
    createChart() {
      console.log(this.min);
      let margin = { top: 10, right: 30, bottom: 30, left: 40 };
      let width = 400 - margin.left - margin.right;
      let height = 400 - margin.top - margin.bottom;

      // append the svg object to the body of the page
      var svg = d3
        .select("#my_dataviz")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
				.attr("transform", "translate(" + margin.left + "," + margin.top + ")");
			
			// Compute summary statistics used for the box:
			let q1 = this.q1 
			let median = this.median
			let q3 = ''
			let interQuantileRange = q3 - q1 
			let min = q1 - 1.5 * interQuantileRange
			let max = q1 + 1.5 * interQuantileRange
    },
  },
  mounted() {
    this.createChart();
  },
};
</script>

<style scoped>
</style>
