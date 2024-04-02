function reverse_int(n){
    const reversed_int = n.toString().split("").reverse().join("");
    return parseInt(reversed_int) * Math.sign(n);
}

console.log(reverse_int(261266));