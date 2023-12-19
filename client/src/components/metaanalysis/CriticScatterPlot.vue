<template>
  <div>
    <div id="criticViz"></div>
  </div>
</template>

<script>
import * as d3 from "d3";

export default {
  name: "CriticScatterPlot",
  props: {
    CriticData: {
      type: Object,
      required: true,
    },
  },
  mounted() {
    this.createScatterPlot();
  },
  watch: {
    CriticData: {
      handler: "createScatterPlot",
      deep: true,
    },
  },
  methods: {
    createScatterPlot() {
      // remove the old chart
      d3.select("#criticViz svg").remove();

      // set the dimensions and margins of the graph
      let margin = { top: 10, right: 30, bottom: 30, left: 60 };
      let width = 460 - margin.left - margin.right;
      let height = 400 - margin.top - margin.bottom;

      // append the svg object to the body of the page
      let svg = d3
        .select("#criticViz")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

      // Add X axis
      let x = d3.scaleLinear().domain([0, 100]).range([0, width]);
      svg
        .append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));

      // Add Y axis
      let y = d3.scaleLinear().domain([0, 100]).range([height, 0]);
      svg.append("g").call(d3.axisLeft(y));

      // Add dots
      svg
        .append("g")
        .selectAll("dot")
        .data(this.CriticData["Data"])
        .enter()
        .append("circle")
        .attr("cx", function (d) {
          return x(d);
        })
        .attr("cy", function (d) {
          return y(d);
        })
        .attr("r", 3)
        .style("fill", "#69b3a2");
    },
  },
};
</script>

<style scoped>
</style>