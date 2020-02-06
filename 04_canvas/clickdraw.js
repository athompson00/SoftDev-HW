var clear = document.getElementById('clear');
var dot = document.getElementById('dot');
var rect = document.getElementById('rect');
var slate = document.getElementById("slate");

var mouseX;
var mouseY;
var mode = "rect";

var clearCanvas = function(e) {
  var ctx = slate.getContext("2d");
  ctx.clearRect(0, 0, 600, 600);
}

var changeMode = function(e) {
  if (mode === "rect")
    mode = "dot";
  else
    mode = "rect";
}

var draw = function(e) {
  var x = e.clientX;
  var y = e.clientY;
  console.log(x);
  console.log(y);
}

slate.addEventListener("click", draw);
clear.addEventListener("click", clearCanvas);
dot.addEventListener("click", changeMode);
rect.addEventListener("click", changeMode);
