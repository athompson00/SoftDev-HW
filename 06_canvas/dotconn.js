var lastPoint = [0, 0];

var clear = document.getElementById('clear');

var clearCanvas = function(e) {
  ctx.clearRect(0, 0, 600, 600);
  lastPoint = [0, 0];
}

clear.addEventListener("click", clearCanvas);

var playground = document.getElementById("playground");



var ctx = playground.getContext("2d");

var draw = function(e){
  //console.log("ran draw");
  var barrier = playground.getBoundingClientRect();
  var x = e.clientX - barrier.left;// here I used getBoundingClientRect which gets the boundaries of the selected element (this time being the canvas). e.ffset if the same idea. it gets the x value adjusting for the offset automatically
  var y = e.clientY - barrier.top;
  if (lastPoint[0] == 0){
    ctx.beginPath();
    lastPoint[0] = x;
    lastPoint[1] - y;
  } else {
    ctx.lineTo(x,y);
    ctx.stroke();
  }
  ctx.beginPath();
  ctx.arc(x, y, 5, 0, Math.PI * 2);
  ctx.fill();
  ctx.moveTo(x, y);

}

playground.addEventListener("click", draw);
