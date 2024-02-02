// Get references to various HTML elements using their IDs
// Reference to the form
const signupForm = document.getElementById("signupForm");
// Reference to the first name input field
const FnameInput = document.getElementById("firstName");
// Reference to the last name input field
const LnameInput = document.getElementById("lastName");
// Reference to the email input field
const emailInput = document.getElementById("email");
// Reference to the age input field
const ageInput = document.getElementById("age");
// Reference to the password input field
const passwordInput = document.getElementById("password");
// Reference to the element displaying password strength
const passwordStrengthDisplay = document.getElementById("passwordStrength");
// Reference to the confirm password input field
const repeatPass = document.getElementById("confirmPassword");
// Reference to the submit button
const submit = document.getElementById("submit");

passwordInput.addEventListener("input", function () {
  const password = passwordInput.value;
  const strength = calculatePasswordStrength(password);
  if (strength == "25" || strength == "") {
    passwordStrengthDisplay.textContent = `Password Strength: weak`;
  } else if (strength == "50") {
    passwordStrengthDisplay.textContent = `Password Strength: moderate`;
  } else if (strength == "75") {
    passwordStrengthDisplay.textContent = `Password Strength: good`;
  } else if (strength == "100") {
    passwordStrengthDisplay.textContent = `Password Strength: excellent`;
  }
  if (passwordInput.value == "") {
    passwordStrengthDisplay.textContent = ``;
  }
});

function calculatePasswordStrength(password) {
  // Simple password strength calculation
  const hasUpperCase = /[A-Z]/.test(password);
  const hasLowerCase = /[a-z]/.test(password);
  const hasNumbers = /\d/.test(password);
  const hasSpecialChars = /[!@#$%^&*(),.?":{}|<>]/.test(password);

  const strength =
    (hasUpperCase + hasLowerCase + hasNumbers + hasSpecialChars) / 4;

  // Map strength value to a percentage (0% to 100%)
  return Math.min(strength * 100, 100);
}
// make submit button disabled on load or inputs are empty
signupForm.onmousemove = () => {
  if (
    FnameInput.value === "" ||
    LnameInput.value === "" ||
    emailInput.value === "" ||
    ageInput.value === "" ||
    passwordInput === ""
  ) {
    submit.disabled = true;
    submit.classList.add("disabled-btn");
  }
};
// check if two passwords is same
repeatPass.addEventListener("input", function () {
  if (passwordInput.value === repeatPass.value) {
    submit.disabled = false;
    submit.classList.remove("disabled-btn");
  } else if (
    passwordInput.value === "" ||
    passwordInput.value !== repeatPass.value
  ) {
    if (passwordInput.value !== repeatPass.value) {
      passwordStrengthDisplay.innerHTML = `Password not Match <i class="fa-solid fa-triangle-exclamation" style="color: red;"></i>`;
    } else if (passwordInput.value === "") {
      passwordWrongDisplay.innerHTML = ``;
    }
    submit.disabled = true;
    submit.classList.add("disabled-btn");
  }
});
document
  .getElementById("signupForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();
  });

fetch("https://restcountries.com/v2/all")
  .then((response) => response.json())
  .then((data) => {
    const countrySelect = document.getElementById("country");

    // Sort countries alphabetically by name
    const sortedCountries = data.sort((a, b) => a.name.localeCompare(b.name));

    // Populate the dropdown with sorted countries
    sortedCountries.forEach((country) => {
      const option = document.createElement("option");
      option.value = country.alpha2Code; // You can use alpha2Code or other properties as needed
      option.textContent = country.name;
      countrySelect.appendChild(option);
    });
  })
  .catch((error) => console.error("Error fetching countries:", error));
