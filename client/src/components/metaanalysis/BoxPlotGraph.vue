<template>
  <div>
    <!-- {{items}} -->
    <div id="my_dataviz"></div>
  </div>
</template>

<script>
import * as d3 from "d3";
import d3Tip from "d3-tip";

export default {
  data() {
    // Assign the prop to a data element for modification
    return {
      score_data: this.items["Data"],
      median: this.items["median"],
      min: this.items["data_set_min"],
      max: this.items["Data_set_Max_Value"],
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
      let margin = { top: 10, right: 30, bottom: 30, left: 40 };
      let width = 400 - margin.left - margin.right;
      let height = 400 - margin.top - margin.bottom;
      let last_value = this.score_data.pop()


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
      let min = this.min;
      let max = this.max;

      let y = ''
      // Show the Y scale
      if (last_value <= 10){
        y = d3.scaleLinear().domain([0, 10]).range([height, 0]);
      }
      else {
        y = d3.scaleLinear().domain([0, 100]).range([height, 0]);
      }
        
      svg.call(d3.axisLeft(y));

      // a few features for the box
      var center = 75;
      var boxWidth = 100;

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
        .attr("x", center - boxWidth / 2)
        .attr("y", y(q3))
        .attr("height", y(q1) - y(q3))
        .attr("width", boxWidth)
        .attr("stroke", "black")
        .style("fill", "#69b3a2");

      // show median, min and max horizontal lines
      svg
        .selectAll("toto")
        .data([min, median, max])
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

      // Add x-axis label
      svg
        .append("text")
        .attr("x", width / 2)
        .attr("y", 125) // Adjust the position as needed
        .style("text-anchor", "middle")
        .text("X-Axis Label")
        .style("font-size", "14px")
        .style("font-color", "black")

      // Initialize D3-tip
      const tip = d3Tip().attr("class", "d3-tip").offset([-10, 0]);

      // Call the tip function on the SVG container
      svg.call(tip);

      // Add tooltips to your box plot elements (e.g., boxes, medians, etc.)
      svg
        .selectAll("toto")
        .on("mouseover", function (d) {
          console.log(d);
          // Show the tooltip when mouseover occurs
          tip.show(d, this);
        })
        .on("mouseout", function () {
          // Hide the tooltip when mouseout occurs
          tip.hide();
        });
    },
  },
  mounted() {
    this.createChart();
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
