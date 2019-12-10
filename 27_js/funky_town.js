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
    return a / b;
  }
}
