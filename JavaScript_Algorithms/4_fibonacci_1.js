const fib = (n) => {
    if( n <= 2){
        return 1
    }
    return fib(n - 1) + fib(n - 2)
}

console.log(fib(3))
console.log(fib(50))
/**
this code is not optimized
a seen above, the result of the second  console log
request comes after a long time
*/