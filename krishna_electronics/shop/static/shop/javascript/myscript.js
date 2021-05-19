var slideIndex = 0;
var sidemenu_product_submenu_flag = 0;
showSlides();

function showSlides() {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}    
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
  setTimeout(showSlides, 3000); // Change image every 2 seconds
}

function openNav()
{
  document.getElementById("mySideNav").style.width = "75%";
}

function closeNav()
{
  document.getElementById("mySideNav").style.width = "0";
}


function close_product_submenu()
{
  if(sidemenu_product_submenu_flag===1)
  {
    document.getElementById("sidemenu_product_submenu").style.display = "none";
    sidemenu_product_submenu_flag = 0;
  }
  else
  {
    document.getElementById("sidemenu_product_submenu").style.display = "block";
    sidemenu_product_submenu_flag = 1;
  }
}

