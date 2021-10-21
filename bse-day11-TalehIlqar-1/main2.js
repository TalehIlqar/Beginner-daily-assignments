let word = prompt("write word");
let letter = prompt("write letter");
let iterator = 0

function search(soz, herf){
    for (let t of soz){
        if (herf == t){
            iterator += 1
        }
        
    }
}
search(word, letter)
console.log(iterator)