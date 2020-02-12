var clear = document.getElementById('clear');
var mode = document.getElementById('mode');
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
    mode.innerHTML = "Toggle: mode dot";
  else
    mode = "rect";
    mode.innerHTML = "Toggle: mode rect";
}

var draw = function(e) {
  var barrier = slate.getBoundingClientRect();
  var x = e.clientX - barrier.left;
  var y = e.clientY - barrier.top;
  console.log(x);
  console.log(y);
  var ctx = slate.getContext("2d");
  if (mode == "rect"){
    ctx.fillRect(x, y, 50, 50);
  } else {
    ctx.beginPath();
    ctx.arc(x, y, 10, 0, Math.PI * 2);
    ctx.fill();
    // ctx.stroke();
  }
}

slate.addEventListener("click", draw);
clear.addEventListener("click", clearCanvas);
mode.addEventListener("click", changeMode);
