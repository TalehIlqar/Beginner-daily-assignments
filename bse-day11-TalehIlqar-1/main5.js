let guess = parseInt(prompt("Count write"));

function myArray(ae) {
    let bosh_list = []
    while (ae >= 25) {
        ae -= 25
        bosh_list.push(25)
    }
    while (ae >= 10) {
        ae -= 10
        bosh_list.push(10)
    }
    while (ae >= 5) {
        ae -= 5
        bosh_list.push(5)
    }
    while (ae >= 2) {
        ae -= 2
        bosh_list.push(2)
    }
    while (ae >= 1) {
        ae -= 1
        bosh_list.push(1)
    }
    return bosh_list
}

myArray(guess)
console.log(myArray(guess))




