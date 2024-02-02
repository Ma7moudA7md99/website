// get form input fields
const form = document.getElementById("analysis");
// get the input fields
const user_inputs = form.getElementsByTagName("input");
// get spans
const animation_spans = form.getElementsByTagName("span");
// get upload button and label
var fileInput = document.getElementById("uploadImage");

var fileLabel = document.getElementById("fileLabel");

for (let i = 0; i < user_inputs.length; i++) {
  user_inputs[i].addEventListener("focus", () => {
    animation_spans[i].style.width = "100%";
  });
}

for (let i = 0; i <= user_inputs.length; i++) {
  user_inputs[i].addEventListener("blur", () => {
    animation_spans[i].style.width = "0";
  });
}

function displayFilename() {
  if (fileInput.files.length > 0) {
    fileLabel.innerHTML = fileInput.files[0].name;
  } else {
    fileLabel.innerHTML = "No file chosen";
  }
}
