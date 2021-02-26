// Scroll code from W3S
// Get button to scroll back to top of the page
let scrollBtn = document.getElementById("scrollToTopMUsers");

window.onscroll = function() {
    showScrollBtn();
};

// Show button when user scrolls down 20px from top of page
function showScrollBtn() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    scrollBtn.style.display = "block";
  } else {
    scrollBtn.style.display = "none";
  }
}

// On button click, scroll to the top of the page 
function scrollUp() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

document.getElementById("scrollToTopMUsers").addEventListener("click", scrollUp);
