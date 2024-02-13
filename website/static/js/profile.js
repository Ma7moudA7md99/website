// get the section
const section = document.getElementsByTagName("section");
// get p the container of input and label
const pContiner = document.querySelectorAll("form p");
// get the username field
const usernameInput = document.getElementById("id_username");
// get all input fields in page
const inputs = document.querySelectorAll("form input");
// gel select fields
const selects = document.querySelectorAll("select");
// get cancel edit icon
const cancelEditIcon = document.getElementById("cancel_icon");
// get start edit icon
const startEditIcon = document.getElementById("enable_icon");
// get the form button
const button = document.getElementById("submit");

for (let i = 0; i < inputs.length; i++) {
  inputs[i].setAttribute("disabled", "true");
}
for (let i = 0; i < selects.length; i++) {
  selects[i].setAttribute("disabled", "true");
}
for (let i = pContiner.length - 4; i < pContiner.length; i++) {
  pContiner[i].classList.add("d-none");
}
button.style.display = "none";

function startEdit() {
  for (let i = 0; i < inputs.length; i++) {
    inputs[i].removeAttribute("disabled");
    inputs[i].style.border = "1px solid var(--main-color)";
  }
  for (let i = 0; i < selects.length; i++) {
    selects[i].removeAttribute("disabled");
    selects[i].style.border = "1px solid var(--main-color)";
  }
  for (let i = pContiner.length - 4; i < pContiner.length; i++) {
    pContiner[i].classList.remove("d-none");
  }
  section[0].classList.add("a-center");
  usernameInput.setAttribute("disabled", "true");
  usernameInput.style.border = "1px solid transparent";
  button.style.display = "block";
  startEditIcon.style.display = "none";
  cancelEditIcon.style.display = "block";
}
function cancelEdit() {
  for (let i = 0; i < inputs.length; i++) {
    inputs[i].setAttribute("disabled", "true");
    inputs[i].style.border = "1px solid transparent";
  }
  for (let i = 0; i < selects.length; i++) {
    selects[i].setAttribute("disabled", "true");
    selects[i].style.border = "1px solid transparent";
  }
  for (let i = pContiner.length - 4; i < pContiner.length; i++) {
    pContiner[i].classList.add("d-none");
  }
  section[0].classList.remove("a-center");
  button.style.display = "none";
  startEditIcon.style.display = "block";
  cancelEditIcon.style.display = "none";
}

AOS.init();
