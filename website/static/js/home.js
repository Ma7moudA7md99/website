// Get the body element
const body = document.getElementById("body");
// Get the flying-btn button
const fly_btn = document.getElementById("flying-btn");
// Get the sign-in div
const sign_in = document.getElementById("sign-in");
// Get the overlay div
const overlay = document.getElementById("overlay");
// Get the sign-in-exit icon
const sign_in_exit = document.getElementById("exit-icon");
// get services cards
const cards = document.getElementsByClassName("card");
// get links inside the cards
const cardLinks = document.getElementsByClassName("service-link");

// show/hide sign-in menu on click of the button
window.addEventListener("scroll", function () {
  if (window.scrollY > 0) {
    fly_btn.style.animation = "rotation-show 2s alternate";
    fly_btn.style.right = "10%";
  } else {
    fly_btn.style.animation = "rotation-hide 2s alternate";
    fly_btn.style.right = "-10%";
  }
});
// show / hide sign in div
fly_btn.onclick = function () {
  if (sign_in.style.left === "-100%" || sign_in.style.left === "") {
    sign_in.style.left = "10%";
    overlay.style.left = "0";
    fly_btn.style.display = "none";
    body.classList.add("sign-in-opened");
  } else {
    sign_in.style.left = "-100%";
    overlay.style.left = "-100%";
    body.classList.remove("sign-in-opened");
  }
};
sign_in_exit.onclick = function () {
  sign_in.style.left = "-100%";
  fly_btn.style.display = "block";
  overlay.style.left = "-100%";
  body.classList.remove("sign-in-opened");
};

// enable / disable link in services card
for (let i = 0; i < cards.length; i++) {
  setTimeout(() => {
    cards[i].addEventListener("mouseover", () => {
      cardLinks[i].style.visibility = "visible";
      cardLinks[i].style.opacity = "1";
    });
    cards[i].addEventListener("mouseout", () => {
      cardLinks[i].style.visibility = "hidden";
      cardLinks[i].style.opacity = "0";
    });
  }, 1600);
}
// AOS initialize
AOS.init();
