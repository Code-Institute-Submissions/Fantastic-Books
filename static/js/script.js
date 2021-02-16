 document.addEventListener('DOMContentLoaded', function () {
     let sidenavs = document.querySelectorAll(".sidenav");
     let sidenavsInstance = M.Sidenav.init(sidenavs, {edge: "right"});
     let collapsibles = document.querySelectorAll(".collapsible");
     let collapsiblesInstance = M.Collapsible.init(collapsibles);
     let modals = document.querySelectorAll('.modal');
     let modalInstances = M.Modal.init(modals);
     let flashMessage = document.getElementById("flashMessage{{loop.index}}");
setTimeout(function() {
    flashMessage.fadeOut("fast");
}, 2000);
  });

// Tabs code from W3S
  function openTab(evt, tabName) {
  let i,
      tabcontent, 
      tablinks;

  // Change to display first tab on page load
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " active";
}

openBooksTabOnload()
// Open first tab on page load
function openBooksTabOnload()  {
    document.getElementById("books").style.display = "block";
    document.getElementsByClassName("tablinks")[0].classList.add("active");
}

//Scroll code from W3S
//Get button to scroll back to top of the page
scrollBtn = document.getElementById("scrollToTop");

// On button click, scroll to the top of the page 
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}