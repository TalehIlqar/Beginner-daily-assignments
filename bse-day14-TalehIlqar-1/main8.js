$("h1").click(function(){
    h1val = $("h1").text()
    $("body").append(`<br> ${h1val}`)
})