var svg = document.getElementById("img");
var clearButton = document.getElementById("clear");

var clearsvg = function() {
  svg.innerHTML = '';
  prevX = -1;
}

var addDot = function(e) {
    var dim = svg.getBoundingClientRect();
    var clix = e.clientX - dim.left;
    var cliy = e.clientY - dim.top;

    var oncircle = false;
    var color = "blue";
    var index;

    var i;
    for (i = 0; i < svg.children['length']; i++){
      if ((((clix - svg.children[i]['attributes'][0]['value']) ^ 2) + ((cliy - svg.children[i]['attributes'][1]['value']) ^ 2)) < (svg.children[i]['attributes'][2]['value'] ^ 2)) {
        oncircle  = true;
        color = svg.children[i]['attributes']['fill']['value'];
        index = i;
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
      circle.setAttribute("r", 10);
      circle.setAttribute("fill", "black");
      svg.appendChild(circle);
    }
    console.log(clix);
    console.log(cliy);
    console.log(oncircle);
}


svg.addEventListener("click", addDot);
clearButton.addEventListener("click", clearsvg);
