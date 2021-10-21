$('#check1').change(function() {
    if($(this).is(":checked")) {
        $("label").text("checked")
    }

    else{
        $("label").text("unchecked")
    }
});