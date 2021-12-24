$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('select').formSelect();
    $('input#input_text, textarea#textarea2').characterCounter();
    $('.parallax').parallax();
  });