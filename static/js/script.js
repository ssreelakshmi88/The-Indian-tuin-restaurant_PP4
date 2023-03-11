// nav hide 
// nav hide 
var navBar = document.querySelectorAll(".nav-link");
var navCollapse = document.querySelector(".navbar-collapse.collapse");
navBar.forEach(function (a) {
    a.addEventListener("click", function () {
        navCollapse.classList.remove("show");
    });
});