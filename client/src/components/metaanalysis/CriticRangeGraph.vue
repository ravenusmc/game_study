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
      q1: this.items["lower_qualtile"],
      q3: this.items["upper_qualtile"],
    };
  },
  props: {
    items: {
      type: Object,
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
      let q1 = this.q1;
      let median = this.median;
      let q3 = this.q3;
      let interQuantileRange = q3 - q1;
      let min = q1 - 1.5 * interQuantileRange;
      let max = q1 + 1.5 * interQuantileRange;

      // Show the Y scale
      var y = d3.scaleLinear()
        .domain([0, 100])
        .range([height, 0]);
      svg.call(d3.axisLeft(y));

      // a few features for the box
      var center = 200;
      var widt = 100;

      // Show the main vertical line
      svg
        .append("line")
        .attr("x1", center)
        .attr("x2", center)
        .attr("y1", y(min))
        .attr("y2", y(max))
        .attr("stroke", "black");

      // Show the box
      svg
        .append("rect")
        .attr("x", center - widt / 2)
        .attr("y", y(q3))
        .attr("height", y(q1) - y(q3))
        .attr("width", widt)
        .attr("stroke", "black")
        .style("fill", "#69b3a2");

      // show median, min and max horizontal lines
      svg
        .selectAll("toto")
        .data([min, median, max])
        .enter()
        .append("line")
        .attr("x1", center - widt / 2)
        .attr("x2", center + widt / 2)
        .attr("y1", function (d) {
          return y(d);
        })
        .attr("y2", function (d) {
          return y(d);
        })
        .attr("stroke", "black");
    },
  },
  mounted() {
    this.createChart();
  },
};
</script>

<style scoped>
</style>
