var start = null;
var prev = null;
var rate = 1;
var circleonoff = false;
var dvdonoff = false;
var dvdx = 0;
var dvdy = 0;
var xrate = -1;
var yrate = -1;


var animation = document.getElementById('animation');

var ctx = animation.getContext('2d');

var animatecircle = document.getElementById('circle');

var animatedvd = document.getElementById('dvd');

var stop = document.getElementById('stop');

var radius = 5;


var logo = new Image();

logo.src = "logo_dvd.jpg";

var drawcircle = function(timestamp){
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
  if (circleonoff){
    window.requestAnimationFrame(drawcircle);
  }
}

var stopanim = function(e){
  circleonoff = false;
  dvdonoff = false;
}

var startcircleanim = function(e){

  if (!circleonoff){


    //console.log("calling startanim");
    circleonoff = true;
    dvdonoff = false;
    window.requestAnimationFrame(drawcircle);
  }
}

var startdvdanim = function(e){
    if (!dvdonoff){
      dvdonoff = true;
      circleonoff = false;
      dvdx = Math.random() * (600-90);
      dvdy = Math.random() * (600-60);
      window.requestAnimationFrame(drawdvd);
    } else {
      window.cancelAnimationFrame();
      dvdx = Math.random() * (600 - 90);
      dvdy = Math.random() * (600 - 60);
      window.requestAnimationFrame(drawdvd);
    }
}

var drawdvd = function(e){
  ctx.clearRect(0, 0, 600, 600);
  if (dvdx >= 600 - 90 || dvdx <= 0){
    xrate *= -1;
  }
  if (dvdy >= 600 - 60 || dvdy <= 0){
    yrate *= -1;
  }
  dvdx += xrate;
  dvdy += yrate;
  ctx.drawImage(logo, dvdx, dvdy, 90, 60);
  if (dvdonoff){
    window.requestAnimationFrame(drawdvd);
  }
}

animatecircle.addEventListener('click', startcircleanim);
stop.addEventListener('click', stopanim);
animatedvd.addEventListener('click', startdvdanim);
