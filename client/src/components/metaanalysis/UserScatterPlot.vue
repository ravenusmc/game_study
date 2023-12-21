<template>
  <div>
    <div id="UserViz"></div>
  </div>
</template>

<script>
import * as d3 from "d3";

export default {
  name: "UserScatterPlot",
  props: {
    UserData: {
      type: Object,
      required: true,
    },
  },
  mounted() {
    this.createScatterPlot();
  },
  watch: {
    UserData: {
      handler: "createScatterPlot",
      deep: true,
    },
  },
  methods: {
    createScatterPlot() {
      // remove the old chart
      d3.select("#UserViz svg").remove();

      // set the dimensions and margins of the graph
      let margin = { top: 10, right: 30, bottom: 30, left: 60 };
      let width = 460 - margin.left - margin.right;
      let height = 400 - margin.top - margin.bottom;

      // append the svg object to the body of the page
      let svg = d3
        .select("#UserViz")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

      // Add X axis
      let x = d3.scaleLinear().domain([0, 10]).range([0, width]);
      svg
        .append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));

      // Add Y axis
      let y = d3.scaleLinear().domain([0, 10]).range([height, 0]);
      svg.append("g").call(d3.axisLeft(y));

      // Add dots
      svg
        .append("g")
        .selectAll("dot")
        .data(this.UserData["Data"])
        .enter()
        .append("circle")
        .attr("cx", function (d) {
          return x(d);
        })
        .attr("cy", function (d) {
          return y(d);
        })
        .attr("r", 3)
        .style("fill", "#69b3a2")
        .on("mouseover", function (event, d) {
          d3.select("#tooltip")
            .style("opacity", 0.9)
            .html("Score: " + d)
            .style("left", event.pageX + "px")
            .style("top", event.pageY - 28 + "px");
        })
        .on("mouseout", function () {
          d3.select("#tooltip").transition().duration(500).style("opacity", 0);
        });

      // Add Y axis label
      svg
        .append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 0 - margin.left)
        .attr("x", 0 - height / 2)
        .attr("dy", "1em")
        .style("text-anchor", "middle")
        .text("Score")
        .style("font-size", "14px")
        .style("fill", "black");
    },
  },
};
</script>

<style scoped>
</style>