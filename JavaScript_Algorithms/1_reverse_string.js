// --- Directions
//We are given a string and required to return a reversed form
 
// example
// given - nevig

function reverse_string(str){
    let reversed_str = "";

    for(let i = 0; i < str.length; i++){
        reversed_str = str[i] + reversed_str;
    }

    return reversed_str;
    //return str.split("").reverse().join("")

}

console.log(reverse_string("this is wonderful"))
