// get input fields
const parent = document.getElementById("contact-left");
const inputs = parent.getElementsByTagName("input");
// get spans
const spans = parent.getElementsByClassName("focus");

// do animation when focus any input
for (let i = 0; i < inputs.length; i++) {
  inputs[i].addEventListener("focus", () => {
    spans[i].style.width = "102.5%";
  });
}
for (let i = 0; i < inputs.length; i++) {
  inputs[i].addEventListener("blur", () => {
    spans[i].style.width = "0%";
  });
}
