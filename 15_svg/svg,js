var svg = document.getElementById("img");
var clearButton = document.getElementById("clear");
var moveButton = document.getElementById("move");
var extraButton = document.getElementById("extra");

var animonoff = false;
var xrate = 1;
var yrate = 1;
var animationid

var isextra

var clearsvg = function() {
  svg.innerHTML = '';
  prevX = -1;
  window.cancelAnimationFrame(animationid);
}

var addDot = function(e) {
    var dim = svg.getBoundingClientRect();
    var clix = e.clientX - dim.left;
    var cliy = e.clientY - dim.top;

    var oncircle = false;
    var color = "black";
    var index;

    var i;

    for (i = 0; i < svg.children['length']; i++){
      var dist = Math.abs(Math.pow((svg.children[i]['attributes'][0]['value'] - clix), 2) + Math.pow((svg.children[i]['attributes'][1]['value'] - cliy), 2)) ;
      if (dist <= 100) {
        oncircle  = true;
        color = svg.children[i]['attributes']['fill']['value'];
        index = i;
        // console.log(dist);
        // console.log(svg.children[i]['attributes'][0]['value']);
        // console.log(svg.children[i]['attributes'][1]['value']);
        // console.log(clix);
        // console.log(cliy);
      }
    }
    if (oncircle) {
      if (color != "blue"){
        svg.children[index].setAttribute("fill", "blue");
      } else {
        svg.children[index].setAttribute('fill', 'black');
        svg.children[index].setAttribute("cx", Math.random() * 500);
        svg.children[index].setAttribute("cy", Math.random() * 500);
      }

    } else {
      circle = document.createElementNS(
      "http://www.w3.org/2000/svg", "circle");
      circle.setAttribute("cx", clix);
      circle.setAttribute("cy", cliy);
      circle.setAttribute('dx', 1);
      circle.setAttribute("dy", 1);
      circle.setAttribute("r", 10);
      circle.setAttribute("fill", "black");
      svg.appendChild(circle);
    }
    // console.log(clix);
    // console.log(cliy);
    console.log(oncircle);
}


var animate = function(e){
  if (animonoff){
    window.cancelAnimationFrame(animationid);
    window.requestAnimationFrame(action);
  } else {
    animonoff = true;
    window.requestAnimationFrame(action);
  }
}

var action = function(e){
  var i;
  for (i = 0; i < svg.children['length']; i++){
    var x = Number(svg.children[i].getAttribute("cx"));
    var y = Number(svg.children[i].getAttribute("cy"));
    var r = Number(svg.children[i].getAttribute("r"));
    var dx = Number(svg.children[i].getAttribute("dx"));
    var dy = Number(svg.children[i].getAttribute("dy"));

    svg.children[i].setAttribute("cx", x + dx);
    svg.children[i].setAttribute("cy", y + dy);

    if (x > Number(svg.getAttribute('width')) -  r || x < r) {
      svg.children[i].setAttribute("dx", - dx);
      svg.children[i].setAttribute("cx", x - dx * 3);
    }
    if (y > Number(svg.getAttribute('height')) -  r || y < r) {
      svg.children[i].setAttribute("dy", - dy);
      svg.children[i].setAttribute("cy", y - dy * 3);
    }
    if (isextra){
      var randomColor = '#'+Math.floor(Math.random()*16777215).toString(16);
      svg.children[i].setAttribute("fill", randomColor);
    }
  }
  if (animonoff){
      animationid = window.requestAnimationFrame(action);
  }
}

var extra = function(e){
  if (isextra){
    isextra = false;
  } else {
    isextra = true;
  }
}



svg.addEventListener("click", addDot);
clearButton.addEventListener("click", clearsvg);
moveButton.addEventListener("click", animate);
extraButton.addEventListener("click", extra);
