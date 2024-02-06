const loginForm = document.getElementsByTagName("form");
const loginInputs = document.getElementsByTagName("input");
const spans = document.querySelectorAll(".container .sign-form div span");

for (let i = 0; i <= loginInputs.length; i++) {
  loginInputs[i].addEventListener("focus", function () {
    spans[i].style.width = "101.5%";
  });
  loginInputs[i].addEventListener("blur", function () {
    spans[i].style.width = "0";
  });
}

AOS.init();
