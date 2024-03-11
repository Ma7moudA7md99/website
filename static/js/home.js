// Get the body element
const body = document.getElementById("body");
// Get the flying-btn button
const fly_btn = document.getElementById("flying-btn");
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

// if (window.innerWidth <= 425) {
//   for (let i = 0; i < cards.length; i++) {
//     if (i % 2 === 0) {
//       cards[i].setAttribute(
//         { "data-aos": "fade-left" },
//         { "data-aos-duration": "800" }
//       );
//     } else {
//       cards[i].setAttribute(
//         { "data-aos": "fade-right" },
//         { "data-aos-duration": "800" }
//       );
//     }
//   }
// }
// AOS initialize
AOS.init();

// doctors slide show
let slideIndex = 0;
showSlides();

function showSlides() {
  let i;
  let slides = document.getElementsByClassName("card-slide");
  for (i = 0; i < slides.length; i++) {
    slides[i].classList.remove("fade-in"); // Remove the fade-in class from all slides
  }
  slideIndex++;
  if (slideIndex > slides.length) {
    slideIndex = 1;
  }
  slides[slideIndex - 1].classList.add("fade-in"); // Apply the fade-in class to the current slide
  setTimeout(showSlides, 2000); // Change image every 2 seconds
}

function plusSlides(n) {
  showSlides((slideIndex += n));
}
