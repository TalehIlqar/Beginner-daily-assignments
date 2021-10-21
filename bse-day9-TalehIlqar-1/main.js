let nama = prompt("Please enter your name");
let price = parseInt(prompt("Please enter price of product"));
let weight = parseInt(prompt("Please enter discount of product"));
let discount = parseInt(prompt("Please enter discount"));
let total = price * weight * discount


document.getElementById("nama").innerHTML = "Name : " + nama
document.getElementById("price").innerHTML = "Price : " + price
document.getElementById("weight").innerHTML = "Weight : " + weight
document.getElementById("discount").innerHTML = "Discount : " + discount
document.getElementById("total").innerHTML = "Total " + total

alert(`Total: ${total}`) 



