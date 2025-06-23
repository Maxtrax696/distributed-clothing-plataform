<<<<<<< HEAD
const baseUrl = "http://localhost:8002/api/login";

document.getElementById("loginForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  const response = await fetch(baseUrl, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ email, password })
  });

  const result = await response.json();

  if (response.ok) {
    document.getElementById("token").value = result.access_token;
    alert("Login successful!");
  } else {
    alert(result.detail || "Login failed");
    document.getElementById("token").value = "";
  }
});

function togglePassword() {
  const field = document.getElementById("password");
  field.type = field.type === "password" ? "text" : "password";
}
=======
document.getElementById("loginForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const email = document.getElementById("email").value.trim();
  const password = document.getElementById("password").value;

  const response = await fetch("/api/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password })
  });

  const resultDiv = document.getElementById("result");

  if (response.ok) {
    const data = await response.json();
    resultDiv.innerHTML = `<div class="alert alert-success">✅ Token: ${data.access_token}</div>`;
  } else {
    const error = await response.json();
    resultDiv.innerHTML = `<div class="alert alert-danger">❌ ${error.detail}</div>`;
  }
});
>>>>>>> qa
