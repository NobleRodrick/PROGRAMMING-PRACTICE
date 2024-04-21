/**
 * 
 * this is a far more effective method, optimized
 * using memoization
 * @param {*} n 
 * @param {*} memo 
 * @returns the fibonacci number at prescribed position
 */
const fib = (n, memo = {}) => {
    if(n in memo){
        return memo[n]
    }
    if(n <= 2){
        return 1
    }
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]
}

console.log(fib(6))
console.log(fib(7))
console.log(fib(8))
console.log(fib(50))
