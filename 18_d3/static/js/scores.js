var sw = false;
// set the dimensions and margins of the graph
var margin = {top: 10, right: 30, bottom: 30, left: 40},
    width = 1000 - margin.left - margin.right,
    height = 600 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg = d3.select("#hist")
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

// get the data
// d3.csv("https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/1_OneNum.csv", function(data) {
d3.csv("static/csv/2010.csv", function(data) {
  console.log(data);
  // X axis: scale and draw:
  var x = d3.scaleLinear()
      .domain([800, 2400])     // can use this instead of 1000 to have the max of data: d3.max(data, function(d) { return +d.price })
      .range([0, width]);
  svg.append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x));

  // set the parameters for the histogram
  var histogram = d3.histogram()
      .value(function(d) { return d.score; })   // I need to give the vector of value
      .domain(x.domain())  // then the domain of the graphic
      .thresholds(x.ticks(70)); // then the numbers of bins

  //console.log(histogram);

  // And apply this function to data to get the bins
  var bins = histogram(data);

  console.log(bins);

  // Y axis: scale and draw:
  var y = d3.scaleLinear()
      .range([height, 0]);
      y.domain([0, d3.max(bins, function(d) { return d.length; })]);   // d3.hist has to be called before the Y axis obviously
  svg.append("g")
      .call(d3.axisLeft(y));

  // append the bar rectangles to the svg element
  svg.selectAll("rect")
      .data(bins)
      .enter()
      .append("rect")
        .attr("x", 1)
        .attr("transform", function(d) { return "translate(" + x(d.x0) + "," + y(d.length) + ")"; })
        .attr("width", function(d) { return x(d.x1) - x(d.x0) -1 ; })
        .attr("height", function(d) { return height - y(d.length); })
        .style("fill", "#69b3a2")

});

var update = function(e){
  //console.log("ran");
  var title = document.getElementById('title');
  var caption = document.getElementById('caption');
  var filename;
  console.log(sw);
  if (!sw){
    filename = "static/csv/2012.csv";
    title.innerHTML = " Average SAT scores by school in NYC 2012 (out of 2400)";
    caption.innerHTML = " Click this button to see 2010 scores in NYC ";
  } else {
    filename = "static/csv/2010.csv";
    title.innerHTML = " Average SAT scores by school in NYC 2010 (out of 2400)";
    caption.innerHTML = " Click this button to see 2012 scores in NYC ";
  }
  sw = !sw;
  d3.csv(filename, function(data) {
    console.log(data);
    var x = d3.scaleLinear()
        .domain([800, 2400])     // can use this instead of 1000 to have the max of data: d3.max(data, function(d) { return +d.price })
        .range([0, width]);
    var histogram = d3.histogram()
        .value(function(d) { return d.score; })   // I need to give the vector of value
        .domain(x.domain())  // then the domain of the graphic
        .thresholds(x.ticks(70)); // then the numbers of bins
    var bins = histogram(data);
    console.log(bins);
    var y = d3.scaleLinear()
        .range([height, 0]);
        y.domain([0, d3.max(bins, function(d) { return d.length; })]);   // d3.hist has to be called before the Y axis obviously

  //  console.log(svg);
    svg.selectAll("rect")
        .data(bins).transition()
          .attr("x", 1)
          .attr("transform", function(d) { return "translate(" + x(d.x0) + "," + y(d.length) + ")"; })
          .attr("width", function(d) { return x(d.x1) - x(d.x0) -1 ; })
          .attr("height", function(d) { return height - y(d.length); })

});
}



var button = document.getElementById('transition');
button.addEventListener("click", update);
