// let iterator = 0;

// for (let i = 0; i <= 1000; i+=15){
//     if (i % 3 == 0 || i % 5 == 0){
//         iterator+=i
//     }
// }
// console.log(iterator)


let iterator = 0;
let i = 0;
while (i <= 1000) {
    if (i % 3 == 0 || i % 5 == 0) {
        iterator += i
    }
    i += 15
    
}
console.log(iterator)



// var i;
// var sayagac = 0;
// for (i = 15; i< 1000; i+=15){
//     sayagac +=i
// }

// document.write(sayagac)
// console.log(sayagac)