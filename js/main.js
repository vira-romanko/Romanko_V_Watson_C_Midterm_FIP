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

  button.addEventListener("click", hamburgerMenu, false);
  searchButton.addEventListener("click", SearchBox, false)

  
    
})();

