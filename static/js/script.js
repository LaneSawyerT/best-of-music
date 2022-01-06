// Materialize functions
$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('select').formSelect();
    $('input#input_text, textarea#textarea2').characterCounter();
    $('.parallax').parallax();
    $('.modal').modal();
    $('.materialboxed').materialbox();
  });

  // Image URL validation
  $document.getElementById("image_url").addEventListener("keyup", check);
  function check() {
      var el = document.getElementById("image_url");
      var button = document.getElementById("submit");
      
      var regex = /\.(jpg|png|gif|bmp)$/i;
      if(regex.test(el.value)) {
          el.classList.remove("valid");
          el.classList.add("invalid");
          button.removeAttribute("disabled");
      } else {
          el.classList.remove("valid");
          el.classList.add("invalid");
          button.setAttribute("disabled", "True");
      }
  }