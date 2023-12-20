<template>
  <div>
    <div id="critic-histogram-chart"></div>
    <div
      id="tooltip"
      style="
        opacity: 0;
        position: absolute;
        pointer-events: none;
        background-color: #fff;
        border: 1px solid #ccc;
        padding: 10px;
        border-radius: 5px;
      "
    ></div>
  </div>
</template>

<script>
import * as d3 from "d3";
import d3Tip from "d3-tip";

export default {
  name: "CriticHistogramGraph",
  props: {
    CriticData: {
      type: Object,
      required: true,
    },
  },
  mounted() {
    this.createHistogram();
  },
  watch: {
    CriticData: {
      handler: "createHistogram",
      deep: true,
    },
  },
  methods: {
    createHistogram() {
      // remove the old chart
      d3.select("#critic-histogram-chart svg").remove();

      // set the dimensions and margins of the graph
      let margin = { top: 10, right: 30, bottom: 30, left: 40 };
      let width = 460 - margin.left - margin.right;
      let height = 400 - margin.top - margin.bottom;

      // append the svg object to the body of the page
      let svg = d3
        .select("#critic-histogram-chart")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

      // X axis: scale and draw:
      let x = d3
        .scaleLinear()
        .domain([0, 100]) // can use this instead of 1000 to have the max of data: d3.max(data, function(d) { return +d.price })
        .range([0, width]);
      svg
        .append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));

      // Add X axis label
      svg
        .append("text")
        .attr(
          "transform",
          "translate(" + width / 2 + " ," + (height + margin.top + 20) + ")"
        )
        .style("text-anchor", "middle")
        .text("Range");

      // set the parameters for the histogram
      let histogram = d3
        .histogram()
        .value(function (d) {
          return d;
        })
        .domain(x.domain())
        .thresholds(x.ticks(10));

      // And apply this function to data to get the bins
      let bins = histogram(this.CriticData["Data"]);

      // Y axis: scale and draw:
      let y = d3.scaleLinear().range([height, 0]);
      y.domain([
        0,
        d3.max(bins, function (d) {
          return d.length;
        }),
      ]);
      svg.append("g").call(d3.axisLeft(y));

      // Add Y axis label
      svg
        .append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 0 - margin.left)
        .attr("x", 0 - height / 2)
        .attr("dy", "1em")
        .style("text-anchor", "middle")
        .text("Frequency");

      // append the bar rectangles to the svg element
      svg
        .selectAll("rect")
        .data(bins)
        .enter()
        .append("rect")
        .attr("x", 1)
        .attr("transform", function (d) {
          return "translate(" + x(d.x0) + "," + y(d.length) + ")";
        })
        .attr("width", function (d) {
          return x(d.x1) - x(d.x0) - 1;
        })
        .attr("height", function (d) {
          return height - y(d.length);
        })
        .style("fill", "#69b3a2")
        .on("mouseover", function (event, d) {
          d3.select("#tooltip")
            .style("opacity", 0.9)
            .html(
              "Range: " + d.x0 + " - " + d.x1 + "<br/>Frequency: " + d.length
            )
            .style("left", event.pageX + "px")
            .style("top", event.pageY - 28 + "px");
        })
        .on("mouseout", function () {
          d3.select("#tooltip").transition().duration(500).style("opacity", 0);
        });
    },
  },
};
</script>

<style scoped>
#tooltip {
  font-size: 12px;
  color: #333;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
}
</style>