
function createTable() {
    let row = parseInt(prompt("say daxil edin"))
    let col = parseInt(prompt("col daxil edin"))
    let table = document.getElementById("myTable");
    for (let i = 0; i < row; i++) {
        let tr = document.createElement("tr")
        table.appendChild(tr)
    
    for (let j = 0; j < col; j++) {
        let td = document.createElement("td")
        td.innerText = ` Row ${i} cell 1 `
        tr.appendChild(td)
    }
}
}
