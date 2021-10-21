let wordLenght = parseInt(prompt("Please, enter number"));

function count(length) {
    let list = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    let sayagac = " "
    for (let i = 0; i < length; i++) {
        let index = Math.floor(Math.random() * list.length)
        sayagac += list[index]
    }
    return sayagac
    
}

let result = count(wordLenght);
console.log(result)




