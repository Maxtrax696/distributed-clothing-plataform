const baseUrl = "http://localhost:8001/api/roles/";

// CREATE
document.getElementById("createForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  const name = document.getElementById("role_name").value;
  const description = document.getElementById("role_description").value;

  const data = { name, description };

  const response = await fetch(baseUrl, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  });

  const result = await response.json();
  alert(result.message || JSON.stringify(result));
  clearForm();
});

// READ (GET)
document.getElementById("getForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  const role_id = document.getElementById("get_role_id").value;

  const response = await fetch(baseUrl + role_id);
  const data = await response.json();

  if (response.ok) {
    document.getElementById("roleDisplay").textContent = JSON.stringify(data, null, 2);
    document.getElementById("role_id").value = data.id;
    document.getElementById("role_name").value = data.name;
    document.getElementById("role_description").value = data.description || "";

    document.getElementById("updateButton").classList.remove("d-none");
    document.getElementById("deleteButton").classList.remove("d-none");
  } else {
    document.getElementById("roleDisplay").textContent = "Error: " + data.detail;
  }
});

// UPDATE
document.getElementById("updateButton").addEventListener("click", async function () {
  const role_id = document.getElementById("role_id").value;
  const name = document.getElementById("role_name").value;
  const description = document.getElementById("role_description").value;

  const data = { name, description };

  const response = await fetch(baseUrl + role_id, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  });

  const result = await response.json();
  alert(result.message || JSON.stringify(result));
  clearForm();
});

// DELETE
document.getElementById("deleteButton").addEventListener("click", async function () {
  const role_id = document.getElementById("role_id").value;
  const confirmed = confirm(`Are you sure you want to delete role ${role_id}?`);
  if (!confirmed) return;

  const response = await fetch(baseUrl + role_id, {
    method: "DELETE"
  });

  const result = await response.json();
  alert(result.message || JSON.stringify(result));
  clearForm();
});

// LIMPIAR FORMULARIO
function clearForm() {
  document.getElementById("role_id").value = "";
  document.getElementById("role_name").value = "";
  document.getElementById("role_description").value = "";
  document.getElementById("roleDisplay").textContent = "";

  document.getElementById("updateButton").classList.add("d-none");
  document.getElementById("deleteButton").classList.add("d-none");
}
