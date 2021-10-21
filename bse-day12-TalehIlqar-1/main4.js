let i = 2;

function insert_Row() {
    i += 1
    let table = document.getElementById("sampleTable");
    let tr = document.createElement("tr")
    let td_first = document.createElement("td")
    let td_second = document.createElement("td")
    td_first.innerText = ` Row ${i} cell 1 `
    td_second.innerText = ` Row ${i} cell 2`
    tr.appendChild(td_first)
    tr.appendChild(td_second)
    table.appendChild(tr)


    
    // table.appendChild(tr)

}

