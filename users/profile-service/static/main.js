<<<<<<< HEAD
function clearForm() {
  document.getElementById("create_user_id").value = "";
  document.getElementById("full_name").value = "";
  document.getElementById("birth_date").value = "";
  document.getElementById("phone_number").value = "";

  
  document.getElementById("createButton").classList.remove("d-none");
  document.getElementById("updateButton").classList.add("d-none");
  document.getElementById("deleteButton").classList.add("d-none");
}

const baseUrl = "http://localhost:8000/api/profiles/";

document.getElementById("createForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  const user_id = parseInt(document.getElementById("create_user_id").value);
  const full_name = document.getElementById("full_name").value;
  const raw_date = document.getElementById("birth_date").value;
  const birth_date = raw_date ? new Date(raw_date).toISOString().slice(0, 10) : null;
  const phone_number = document.getElementById("phone_number").value;

  const data = { user_id, full_name, birth_date, phone_number };

  const response = await fetch(baseUrl, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });

  const result = await response.json();
  alert(result.message || JSON.stringify(result));
  clearForm();
});

document.getElementById("getForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  const user_id = document.getElementById("get_user_id").value;
  const response = await fetch(baseUrl + user_id);
  const data = await response.json();

  if (response.ok) {
    document.getElementById("profileDisplay").textContent = JSON.stringify(data, null, 2);

    // Rellenar el formulario principal
    document.getElementById("create_user_id").value = data.user_id;
    document.getElementById("full_name").value = data.full_name || "";
    document.getElementById("birth_date").value = data.birth_date || "";
    document.getElementById("phone_number").value = data.phone_number || "";

    // Mostrar botones Update y Delete
    document.getElementById("createButton").classList.add("d-none");
    document.getElementById("updateButton").classList.remove("d-none");
    document.getElementById("deleteButton").classList.remove("d-none");
  } else {
    document.getElementById("profileDisplay").textContent = "Error: " + data.detail;
  }
});

// Manejar botón Update
document.getElementById("updateButton").addEventListener("click", async function () {
  const user_id = document.getElementById("create_user_id").value;
=======
document.getElementById("profileForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const user_id = document.getElementById("user_id").value;
>>>>>>> qa
  const full_name = document.getElementById("full_name").value;
  const birth_date = document.getElementById("birth_date").value;
  const phone_number = document.getElementById("phone_number").value;

<<<<<<< HEAD
  const data = {
    full_name: full_name || null,
    birth_date: birth_date || null,
    phone_number: phone_number || null
  };

  const response = await fetch(baseUrl + user_id, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });

  const result = await response.json();
  alert(result.message || JSON.stringify(result));
  clearForm();
  clearForm();
});

// Manejar botón Delete
document.getElementById("deleteButton").addEventListener("click", async function () {
  const user_id = document.getElementById("create_user_id").value;
  const confirmed = confirm(`Are you sure you want to delete user: ${user_id}?`);
  if (!confirmed) return;

  const response = await fetch(baseUrl + user_id, {
    method: "DELETE"
  });

  const result = await response.json();
  alert(result.message || JSON.stringify(result));
  clearForm();
  clearForm();
});
=======
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
>>>>>>> qa
