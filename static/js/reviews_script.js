// Scroll code from W3S
// Get button to scroll back to top of the page
let scrollBtn = document.getElementById("scrollToTop");

window.onscroll = function() {
    showScrollBtn()};

// Show button when user scrolls down 20px from top of page
function showScrollBtn() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    scrollBtn.style.display = "block";
  } else {
    scrollBtn.style.display = "none";
  }
};

// On button click, scroll to the top of the page 
function scrollUp() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

document.getElementById("scrollToTop").addEventListener("click", scrollUp);


/* Hide Clear Results Btn until Search is performed
/*
document.getElementById("search-submit").addEventListener("submit", manageBtn);
document.getElementById("search").addEventListener("input", manageBtn)
*/

document.getElementById("submitBtn").addEventListener("click", manageBtn)

function manageBtn() {
     document.getElementsByClassName("clear").style.display = "block";
};


/* 
let id, 
    i, 
    inputs = document.getElementsByClassName('review-search');
    for (i = 0; i < inputs.length; i++){  
        if (inputs[i].type == 'text' && (inputs[i].value == '' || inputs[i].value == 'n/a'))  {    
            document.getElementById('clear-results' + inputs[i].id).style.display = 'none';  
        };
    };
    */

document.getElementById("submitBtn").onclick = function() {manageBtn()};

function manageBtn() {
  document.querySelectorAll("clear").style.display = "block";
}