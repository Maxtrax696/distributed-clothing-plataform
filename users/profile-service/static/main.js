document.getElementById("profileForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const user_id = document.getElementById("user_id").value;
  const full_name = document.getElementById("full_name").value;
  const birth_date = document.getElementById("birth_date").value;
  const phone_number = document.getElementById("phone_number").value;

  const response = await fetch("/api/profile/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ user_id, full_name, birth_date, phone_number })
  });

  const result = document.getElementById("result");
  const data = await response.json();

  if (response.ok) {
    result.innerHTML = `<div class="alert alert-success">${data.message}</div>`;
  } else {
    result.innerHTML = `<div class="alert alert-danger">Error: ${data.detail}</div>`;
  }
});
