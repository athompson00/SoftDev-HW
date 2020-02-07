//What does e.preventDefault() do?
//Stops an HTML element from performing it's default action


var clear = document.getElementById('clear');
var modeButton = document.getElementById('mode');
var slate = document.getElementById("slate");

var mouseX;
var mouseY;
var mode = "rect";

var clearCanvas = function(e) {
  var ctx = slate.getContext("2d");
  ctx.clearRect(0, 0, 600, 600);
}

var changeMode = function(e) {
  if (mode === "rect"){
    mode = "dot";
    modeButton.innerHTML = " Toggle Mode: Dot";
  }
  else {
    mode = "rect";
    modeButton.innerHTML = " Toggle Mode: Rectangle";
  }
}

var draw = function(e) {
  var barrier = slate.getBoundingClientRect();
  var x = e.clientX - barrier.left;// here I used getBoundingClientRect which gets the boundaries of the selected element (this time being the canvas). e.ffset if the same idea. it gets the x value adjusting for the offset automatically
  var y = e.clientY - barrier.top;
  console.log(x);
  console.log(y);
  var ctx = slate.getContext("2d");
  if (mode == "rect"){
    ctx.fillRect(x, y, 50, 50);
  } else {
    ctx.beginPath(); // initiates a drawing line
    ctx.arc(x, y, 10, 0, Math.PI * 2);
    ctx.fill();
  }
}

slate.addEventListener("click", draw);
clear.addEventListener("click", clearCanvas);
modeButton.addEventListener("click", changeMode);
