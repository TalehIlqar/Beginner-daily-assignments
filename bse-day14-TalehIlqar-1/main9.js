$(document).ready(function(){
    $("input").keydown(function(){
      $("input").css("background-color", "yellow");
    });
    $("input").keyup(function(){
      $("input").css("background-color", "pink");
    });
  });