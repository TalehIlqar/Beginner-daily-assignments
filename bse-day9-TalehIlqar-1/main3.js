let richter = parseFloat(prompt("Please, write richter "));

let Energy = 10 ** (1.5 * richter + 4.8);
let TNT = ( 4.184 * 10 ** 6 );

let result = Energy / TNT

console.log(result)

alert(`Result ${result}`)
document.write(result)