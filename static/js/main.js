// navbar functions
const navbar = document.querySelector(".navbar");
const fly_btn = document.getElementById("flying-btn");
window.addEventListener("scroll", function () {
  if (window.scrollY > 0) {
    navbar.classList.add("set-shadow");
    // fly_btn.classList.add("show-fly-btn");
    fly_btn.style.right = "10%";
  }
  if (window.screenY < 50) {
    fly_btn.style.right = "-100%";
    // fly_btn.classList.remove("show-fly-btn");
  } else {
    navbar.classList.remove("set-shadow");
  }
});

document.addEventListener("DOMContentLoaded", function () {
  const navItems = document.querySelectorAll(".nav-item");
  const sections = document.querySelectorAll("section");

  function toggleActiveClass() {
    const scrollPosition = window.scrollY;

    sections.forEach((section, index) => {
      if (
        scrollPosition >= section.offsetTop - 150 &&
        scrollPosition < section.offsetTop + section.offsetHeight
      ) {
        navItems.forEach((navItem) => navItem.classList.remove("active"));
        navItems[index].classList.add("active");
      }
    });
  }
  window.addEventListener("scroll", toggleActiveClass);
  toggleActiveClass();
});

AOS.init();
