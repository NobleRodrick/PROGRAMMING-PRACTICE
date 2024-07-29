function getAverage(scores) {
    function returnTotal(array){
      return array.length;
    }
  
    function returnSumOfScores(array){
      let sum = 0;
      for(let i = 0; i < array.length; i++){
        sum = sum + array[i];
      }
  
      return sum;
  
    }
  
    let theTotal = returnTotal(scores);
    let theSum = returnSumOfScores(scores);
  
    let average = theSum/theTotal;
  
    return average;
  
  
  }
  
  console.log(getAverage([92, 88, 12, 77, 57, 100, 67, 38, 97, 89]));
  console.log(getAverage([45, 87, 98, 100, 86, 94, 67, 88, 94, 95]));