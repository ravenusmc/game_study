<template>
  <div>
    <!-- {{ items }} -->
    <!-- <div id="my_dataviz"></div> -->
    <div id="UserDataViz"></div>
    <!-- <button @click="updateData()">Update Data</button> -->
  </div>
</template>

<script>
import * as d3 from "d3";
import d3Tip from "d3-tip";

export default {
  props: {
    items: {
      type: Object,
      required: true,
    },
  },
  mounted() {
    this.createChart();
  },
  watch: {
    items: {
      handler: "createChart",
      deep: true,
    },
  },
  methods: {
    createChart() {
      // remove the old chart
      d3.select("#UserDataViz svg").remove();

      let margin = { top: 10, right: 30, bottom: 30, left: 40 };
      let width = 400 - margin.left - margin.right;
      let height = 400 - margin.top - margin.bottom;

      // append the svg object to the body of the page
      var svg = d3
        .select("#UserDataViz")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

      // Compute summary statistics used for the box:
      let interQuantileRange =
        this.items["upper_qualtile"] - this.items["lower_qualtile"];

      let y = "";
      // Set the Y scale
      if (this.items["Data_set_Max_Value"] <= 10) {
        y = d3.scaleLinear().domain([0, 10]).range([height, 0]);
      } else {
        y = d3.scaleLinear().domain([0, 100]).range([height, 0]);
      }

      svg.call(d3.axisLeft(y));

      //a few features for the box
      let center = 75;
      let boxWidth = 100;

      // Show the main vertical line
      svg
        .append("line")
        .attr("x1", center)
        .attr("x2", center)
        .attr("y1", y(this.items["data_set_min"]))
        .attr("y2", y(this.items["Data_set_Max_Value"]))
        .attr("stroke", "black");

      // Show the box
      svg
        .append("rect")
        .attr("x", center - boxWidth / 2)
        .attr("y", y(this.items["upper_qualtile"]))
        .attr(
          "height",
          y(this.items["lower_qualtile"]) - y(this.items["upper_qualtile"])
        )
        .attr("width", boxWidth)
        .attr("stroke", "black")
        .style("fill", "#69b3a2");

      // show median, min and max horizontal lines
      svg
        .selectAll("toto")
        .data([
          this.items["data_set_min"],
          this.items["median"],
          this.items["Data_set_Max_Value"],
        ])
        .enter()
        .append("line")
        .attr("x1", center - boxWidth / 2)
        .attr("x2", center + boxWidth / 2)
        .attr("y1", function (d) {
          return y(d);
        })
        .attr("y2", function (d) {
          return y(d);
        })
        .attr("stroke", "black");

      // Add y-axis label
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
.d3-tip {
  line-height: 1;
  font-weight: bold;
  padding: 12px;
  background: rgba(0, 0, 0, 0.8);
  color: #fff;
  border-radius: 2px;
  pointer-events: none;
}
</style>
