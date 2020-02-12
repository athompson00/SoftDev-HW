var start = null;
var prev = null;
var rate = 1;
var onoff = true;

var animation = document.getElementById('animation');

var ctx = animation.getContext('2d');

var animate = document.getElementById('animate');

var stop = document.getElementById('stop');

var draw = function(timestamp){
  console.log("calling draw");
  if (!start){
    start = timestamp;
  } else {
    ctx.clearRect(0, 0, 600, 600);
  }
  if (radius >= 300 || radius <= 0){
    rate *= -1;
    start = timestamp;
  }
  var radius = radius + (rate * (timestamp - start));
  ctx.beginPath();
  ctx.arc(300, 300, radius, 0, Math.PI * 2);
  ctx.fill();
  if (onoff){
    window.requestAnimationFrame(draw)
  }
}

var stopanim = function(e){
  onoff = false;
}

var startanim = function(e){
  onoff = true;
  //console.log("calling startanim");
  window.requestAnimationFrame(draw);
}

animate.addEventListener('click', startanim);
stop.addEventListener('click', stopanim);
