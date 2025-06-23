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
