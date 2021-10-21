let sade = parseInt(prompt('Enter lower number: '));

function prime(guess) {
    for (let j = 2; j < guess; j++) {
        if (guess % j == 0) {
            return false
        }
    }
    return true
}


if (prime(sade)) {
    console.log("sadedir");
} else {
    console.log("murekkeb");
}