$('input').focus(function () {
    $('input').addClass("focusedin").removeClass("focusedout")
})

$('input').focusout(function () {
    $('input').addClass("focusedout").removeClass("focusedin")
})

