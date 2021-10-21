let guess = parseInt(prompt("Please, enter your guess number"));

let first_num = parseInt(guess / 100)**3
let second_num = parseInt((guess / 10) % 10)**3
let third_num = parseInt(guess % 10)**3

let result = first_num + second_num + third_num
console.log(first_num)
console.log(second_num)
console.log(third_num)
console.log(result)
if (guess == result){
    console.log(`${guess} is Armstrong number`)
}
else{
    console.log(`${guess} isn't Armstrong number`)
}

