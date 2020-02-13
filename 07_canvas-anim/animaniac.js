var start = null;
var prev = null;
var rate = 1;
var onoff = false;

var animation = document.getElementById('animation');

var ctx = animation.getContext('2d');

var animate = document.getElementById('animate');

var stop = document.getElementById('stop');

var radius = 5;

var draw = function(timestamp){
  //console.log("calling draw");
  if (!start){
    start = timestamp;
  } else {
    ctx.clearRect(0, 0, 600, 600);
  }
  if (radius >= 300 || radius <= 0){
    rate *= -1;
  }
  radius = radius + rate;
  ctx.beginPath();
  ctx.arc(300, 300, radius, 0, Math.PI * 2);
  ctx.fill();
  if (onoff){
    window.requestAnimationFrame(draw);
  }
}

var stopanim = function(e){
  onoff = false;
}

var startanim = function(e){

  if (!onoff){


    //console.log("calling startanim");
    onoff = true;
    window.requestAnimationFrame(draw);
  }
}

animate.addEventListener('click', startanim);
stop.addEventListener('click', stopanim);
