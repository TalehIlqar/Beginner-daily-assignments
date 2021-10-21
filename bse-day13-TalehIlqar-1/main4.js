let toTop = document.querySelector("#top");
document.addEventListener("scroll",function(){
    if(window.pageYOffset > window.innerHeight){
        toTop.style.display = "block";
    }else{
        toTop.style.display = "none";
    }
});toTop.addEventListener('click', () => {
    window.scrollTo({top:0, behavior: 'smooth'});
});