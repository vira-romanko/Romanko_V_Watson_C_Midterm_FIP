(function(){
  "use strict";
  
  console.log("fired");

  var button = document.querySelector("#button");
  var burgerCon = document.querySelector("#hamCon");
  var searchButton = document.querySelector(" #search");
  var searchBox = document.querySelector(".searchBox")

  function hamburgerMenu() {
    hamCon.classList.toggle("slideToggle");
    button.classList.toggle("expanded");
  }

  function SearchBox(){
  	searchBox.classList.toggle("slideToggle");
  	searchButton.classList.toggle("expanded");
  }



  //image gallery

  let slider = document.querySelectorAll(".slide"),
  leftArrow = document.querySelector("#arrow-left"),
  rightArrow = document.querySelector("#arrow-right"),
  currentSlide = 0; 

//reset all the images
function reset() {
  for (let i = 0; i < slider.length; i++) {
    slider[i].style.display = "none";
  }
}

// first slider to show
function startSlide() {
  reset();

  slider[0].style.display = "block";
}

// before slider
function slideLeft() {
  reset();
  console.log("previous slide");
  slider[currentSlide - 1].style.display = "block";
  currentSlide--;
}

// After slider snow next one
function slideRight() {
  reset();
  console.log("next slide");
  slider[currentSlide + 1].style.display = "block";
  currentSlide++;
}
//click on left arrow
leftArrow.addEventListener("click", function() {
  if (currentSlide === 0) {
    currentSlide = slider.length;
  }
  slideLeft();
  console.log("you clicked left arrow");
});

// click on right arrow
rightArrow.addEventListener("click", function() {
  if (currentSlide === slider.length - 1) {
    currentSlide = -1;
  }
  slideRight();
  console.log("you clicked right arrow");
});

startSlide();

  button.addEventListener("click", hamburgerMenu, false);
  searchButton.addEventListener("click", SearchBox, false);



  

  
    
})();

