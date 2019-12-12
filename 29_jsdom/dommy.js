var changeHeading = function(e) {
  var h = document.getElementById("h");
  //console.log(e);
  h.innerHTML = e.textContent;
  console.log(e);
};

var removeItem = function(e){

};

var lis = document.getElementsByTagName("li");

for (var i=0; i < lis.length; i++){
  lis[i].addEventListener('mouseover', changeHeading(lis[i]));
  lis[i].addEventListener("mouseout", changeHeading("Hello World!"));
}
