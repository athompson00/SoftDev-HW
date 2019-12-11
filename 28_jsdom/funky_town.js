var fact = function(n){
  if (n == 1){
       return 1;
     }
  return (n * fact(n - 1));
}

var fibonacci = function(n){
  var a = 0;
  var b = 1;
  if (n == 0){
    return 0;
  } else if (n == 1 || n == 2){
    return 1;
  } else {
    return fibonacci(n - 1) + fibonacci(n - 2);
  }
}

var gcd = function(a, b){
  if (b > a){
    return gcd(b, a);
  }
  if (a % b == 0){
    return b;
  } else {
    return gcd(b, a % b);
  }
}



var randomStudent = function(){
  var students = [
  "Loreta", "Lindstrom",
  "Tiffaney", "Barbara",
  "Tarah", "Axford",
  "China", "Piano",
  "Freda", "Dewall",
  "Ramonita", "Grove",
  "Mason", "Forgione",
  "Krystle" ,"Marshburn",
  "Patti", "Lasso",
  "Bud", "Michel",
  "Rodolfo", "Haggett",
  "Terra", "Valencia"
  ];
  var randind = Math.floor(Math.random() * 24);
  return students[randind];
}


var factButton = document.getElementById("factButton").addEventListener("click",
  function factB(){
    var number = parseInt(document.getElementById("factInput").value);
    console.log(fact(number));
    return fact(number);
  })

// var fibButton = document.getElementById("fibButton").addEventListener("click", console.log("clicked"));
