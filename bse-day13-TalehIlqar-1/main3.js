let bod = document.getElementById("body");

document.addEventListener("scroll", function() {
    let d = new Date();
    let p = document.createElement("p");
    p.innerHTML = d;
    bod.appendChild(p)
});

