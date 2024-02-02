// get input fields
const inputs = document.getElementsByTagName("input");
// get spans
const spans = document.getElementsByClassName("focus");

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
