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
  console.log(students);
  var randind = Math.floor(Math.random() * 24);
  return students[randind];
}
