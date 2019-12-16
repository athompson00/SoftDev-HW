//changes heading of html file
var changeHeading = function(e) {
  var h = document.getElementById("h");
  h.innerHTML = e.target.innerHTML;
};

//removes an item from regular list
var removeItem = function(e) {
  e.target.remove();
};

//dynamic list items
var lis = document.getElementsByTagName("li");

for (var i=0; i<lis.length; i++) {
  console.log(lis[i].textContent);
  lis[i].addEventListener('mouseover', changeHeading);
  lis[i].addEventListener('mouseout', () => {
    document.getElementById("h").innerHTML = "Hello World!";
  });
  lis[i].addEventListener('click', removeItem);
};



//add an item to regular list
var currentNum = 7;
var getNextItem = function() {
  currentNum += 1;
  currentItem = "item " + currentNum;
  console.log(currentItem);
};

var addItem = function(e) {
  var list = document.getElementById("thelist")
  var item = document.createElement("li")
  getNextItem();
  console.log(currentItem);
  item.appendChild(document.createTextNode(currentItem));
  list.appendChild(item);
  item.addEventListener('mouseover', changeHeading);
  item.addEventListener('click', removeItem);
};

var button = document.getElementById("b");
button.addEventListener('click', addItem);

//add an item to fib list
var currentTerm = 0

var fib = function(n) {
  if (n < 2) {
    return 1;
  }
  else {
    return fib(n-1) + fib(n-2);
  }
};

var addFib = function(e) {
  console.log(currentTerm);
  var list = document.getElementById("fiblist")
  var item = document.createElement("li")
  item.appendChild(document.createTextNode(fib(currentTerm)));
  list.appendChild(item);
  currentTerm += 1;
};

var addFib2 = function(e) {
    var lis = document.getElementById("fiblist");
    var ch = lis.childNodes;
    var item = document.createElement("li");
    var len = children.length;

    if (len > 2) {
	     item.innerHTML = parseInt(ch[len - 2].innerHTML) + parseInt(ch[len - 1].innerHTML);
    } else {
	     item.innerHTML = "1";
    }
    lis.appendChild(item);
}

var fb = document.getElementById("fb");
fb.addEventListener("click", addFib);
