const navbar = document.querySelector(".navbar");

window.addEventListener("scroll", function () {
  if (window.scrollY > 0) {
    navbar.classList.add("set-shadow");
  } else {
    navbar.classList.remove("set-shadow");
  }
});
