var start = null;//for drawcircle
var rate = 1;//rate of radius change
var circleonoff = false;//whether or not circle anim is on
var dvdonoff = false;//whether or not dvd anim is on
//both begin off
var dvdx = 0;//dvd anim xcor
var dvdy = 0;//dvd anim ycor
var xrate = -1;//dvd xrate of change
var yrate = -1;//dvd yrate of change


var animation = document.getElementById('animation');//canvas

var ctx = animation.getContext('2d');//cursor

var animatecircle = document.getElementById('circle');//im an animaniac button

var animatedvd = document.getElementById('dvd');//im waiting for the movie button

var stop = document.getElementById('stop');//stop button

var radius = 5;//circle radius for animaniac animation


var logo = new Image(); //declaring image for use on canvas

logo.src = "logo_dvd.jpg";//source of dvd image

var drawcircle = function(timestamp){
  //console.log("calling draw");
  if (!start){
    start = timestamp;
  } else {
    ctx.clearRect(0, 0, 600, 600);//clears current image
  }
  if (radius >= 300 || radius <= 0){
    rate *= -1;//negates rate of change of radius
  }
  radius = radius + rate;//adjusting radius
  ctx.beginPath();
  ctx.arc(300, 300, radius, 0, Math.PI * 2);//drawing circle
  ctx.fill();
  if (circleonoff){
    window.requestAnimationFrame(drawcircle);//recursively calling new animation frame as long as the circle anim is on
  }
}

var stopanim = function(e){
  //stops all anims
  //new anim frames will not be called
  circleonoff = false;
  dvdonoff = false;
}

var startcircleanim = function(e){

  if (!circleonoff){//if it's off


    //console.log("calling startanim");
    circleonoff = true;//turn it on
    dvdonoff = false;//turn other anim off
    window.requestAnimationFrame(drawcircle);//begin animation
  }
}

var startdvdanim = function(e){
    if (!dvdonoff){//if it's off
      dvdonoff = true;//turn it on
      circleonoff = false;//turn off other anim
      //get random position for dvd to start
      dvdx = Math.random() * (600-90);
      dvdy = Math.random() * (600-60);
      //call animation
      window.requestAnimationFrame(drawdvd);
    } else {//if it's on
      window.cancelAnimationFrame();//cancel previous anim frame
      //repeat above
      dvdx = Math.random() * (600 - 90);
      dvdy = Math.random() * (600 - 60);
      window.requestAnimationFrame(drawdvd);
    }
}

var drawdvd = function(e){
  ctx.clearRect(0, 0, 600, 600);//clear canvas
  if (dvdx >= 600 - 90 || dvdx <= 0){//when xcor hits edge
    xrate *= -1;//negate it
  }
  if (dvdy >= 600 - 60 || dvdy <= 0){//when ycor hits edge
    yrate *= -1;//negate it
  }
  //applying rate adjustments
  dvdx += xrate;
  dvdy += yrate;
  //drawing image at specified coords
  ctx.drawImage(logo, dvdx, dvdy, 90, 60);
  if (dvdonoff){//if the anim is still on
    window.requestAnimationFrame(drawdvd);//call next frame
  }
}

animatecircle.addEventListener('click', startcircleanim);//animaniac button
stop.addEventListener('click', stopanim);//stop button
animatedvd.addEventListener('click', startdvdanim);//waitiing for movie button
