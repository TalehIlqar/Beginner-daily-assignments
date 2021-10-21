let word = prompt("yazin")

let arr = word.split(',');

function sum(list) {
    let max = 0;
    for (let i = 0; i < list.length; i++) {
        let hi = list[i].length;
        if (hi > max) {
            max = hi
        }
    }
    for (let w of list) {
        if (w.length == max) {
            return w

        }
    }
}
result = sum(arr)
console.log(result)

