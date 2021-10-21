let li = document.querySelectorAll('.li')


li.forEach((element) =>{
    element.addEventListener("click", function(event){
        if (!event.ctrlKey){
            li.forEach((element) =>{
                element.classList.remove("selected")
            });
        }
        this.classList.add("selected")
    });
});

