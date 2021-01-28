//Array flattenr activity
// Define a function arrayFlattener with a 2 dimensional array as parameter:
// example of 2 dimensional array: [1,[2,3],4,5]

//Return a new 1 dimensional array like, [1,2,3,4]

//your code here
function arrayFlattener(x) {
  const array = [];
  for (let i=0; i<x.length; i++) {
    if (x[i].length > 0){

      for (let j=0; j<x[i].length; j++) {
      array.push(x[i][j]);
      }
    }
      else {
      array.push(x[i]);
    }
  }
  return array;
}
 
//uncomment next line one by one, then check the console for results
console.log(arrayFlattener([1,[2,3],4,5]))

//don't change this line
if (typeof module !== "undefined") {
  module.exports = {
    arrayFlattener,
  };
}