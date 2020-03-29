var svg = document.getElementById("img");
var clearButton = document.getElementById("clear");
var prevX = -1;
var prevY;

var clearsvg = function() {
  svg.innerHTML = '';
  prevX = -1;
}

var addDot = function(e) {
  if (prevX == -1) {
    prevX = e.offsetX;
    prevY = e.offsetY;

    circle = document.createElementNS(
    "http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("cx", e.offsetX);
    circle.setAttribute("cy", e.offsetY);
    circle.setAttribute("r", 5);
    circle.setAttribute("fill", "black");

    svg.appendChild(circle);
  } else {

    line = document.createElementNS(
    "http://www.w3.org/2000/svg", "line");
    line.setAttribute("x1", prevX);
    line.setAttribute("y1", prevY);
    line.setAttribute("x2", e.offsetX);
    line.setAttribute("y2", e.offsetY);
    line.setAttribute("stroke", "black");

    circle = document.createElementNS(
    "http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("cx", e.offsetX);
    circle.setAttribute("cy", e.offsetY);
    circle.setAttribute("r", 5);
    circle.setAttribute("fill", "black");

    prevX = e.offsetX;
    prevY = e.offsetY;

    svg.appendChild(line);
    svg.appendChild(circle);
  }
}

svg.addEventListener("click", addDot);
clearButton.addEventListener("click", clearsvg);
