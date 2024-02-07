// Get the header element
const header = document.getElementById("header");
// Get the mobile-icon for the header
const mobile_icon = document.getElementById("mobile-icon");
// Get the mobile menu in phones
const mobile_menu = document.getElementById("right");
// Get profile image icon
const profIcon = document.getElementById("profile-icon");
// Get profile list items
const profItem = document.getElementById("profile-items");
// show/hide sign-in menu on click of the button
window.addEventListener("scroll", function () {
  if (window.scrollY > 0) {
    header.classList.add("set-shadow");
  } else if (window.scrollY < 3) {
    header.classList.remove("set-shadow");
  }
});

// show / hide menu bar in mobile < 768px size
mobile_icon.onclick = function () {
  if (
    mobile_menu.style.display === "none" ||
    mobile_menu.style.display === ""
  ) {
    mobile_menu.style.display = "block";
  } else {
    mobile_menu.style.display = "none";
  }
};
// show / hide profile list
function showProfileList() {
  profItem.classList.toggle("item-is-active");
}
// AOS initialize
AOS.init();
