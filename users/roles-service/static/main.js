const baseRolesUrl = "http://localhost:8001/api/roles";

let currentUserId = null;
let currentRoleId = null;

const suggestionsBox = document.getElementById("suggestions");
const searchInput = document.getElementById("search_email");

<<<<<<< HEAD
// Autosugerencia al escribir
=======
>>>>>>> qa
searchInput.addEventListener("input", async () => {
  const query = searchInput.value.trim();
  suggestionsBox.innerHTML = "";

  if (query.length < 2) return;

<<<<<<< HEAD
  const res = await fetch(`http://localhost:8003/api/register/search-by-username?username=
    ${encodeURIComponent(query)}`);
=======
  const res = await fetch(`http://localhost:8003/api/register/search-by-username?username=${encodeURIComponent(query)}`);
>>>>>>> qa
  const users = await res.json();

  users.forEach(user => {
    const li = document.createElement("li");
    li.className = "list-group-item list-group-item-action";
    li.textContent = user.email;
    li.addEventListener("click", () => {
      searchInput.value = user.email;
      suggestionsBox.innerHTML = "";
<<<<<<< HEAD
      document.getElementById("searchForm").dispatchEvent(new Event("submit"));
=======
      document.getElementById("searchForm").dispatchEvent(new Event("submit")); // fuerza la búsqueda
>>>>>>> qa
    });
    suggestionsBox.appendChild(li);
  });
});

<<<<<<< HEAD
// Ocultar sugerencias al salir del campo
=======
>>>>>>> qa
searchInput.addEventListener("blur", () => {
  setTimeout(() => suggestionsBox.innerHTML = "", 200);
});

<<<<<<< HEAD
// Buscar usuario y roles
=======
>>>>>>> qa
document.getElementById("searchForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const email = document.getElementById("search_email").value;
  const userInfoDiv = document.getElementById("userInfo");
  const rolesDiv = document.getElementById("userRoles");
  const roleSelect = document.getElementById("role_select");
  const updateBtn = document.getElementById("updateBtn");

  userInfoDiv.innerHTML = "";
  rolesDiv.innerHTML = "";
  roleSelect.innerHTML = '<option value="">Selecciona un rol</option>';
  updateBtn.disabled = true;

<<<<<<< HEAD
  // Buscar usuario por correo
  const userRes = await fetch(`http://localhost:8003/api/register/email/
    ${encodeURIComponent(email.trim())}`);
  if (!userRes.ok) {
    userInfoDiv.innerHTML = `<div class="alert alert-danger"> Usuario no encontrado.</div>`;
=======
  const userRes = await fetch(`http://localhost:8003/api/register/email/${encodeURIComponent(email.trim())}`);
  if (!userRes.ok) {
    userInfoDiv.innerHTML = `<div class="alert alert-danger">❌ Usuario no encontrado.</div>`;
>>>>>>> qa
    return;
  }

  const user = await userRes.json();
  currentUserId = user.id;
  document.getElementById("update_user_id").value = user.id;

  userInfoDiv.innerHTML = `
    <div class="alert alert-light">
      <strong>Nombre:</strong> ${user.first_name} ${user.last_name} <br>
      <strong>Email:</strong> ${user.email}
    </div>
  `;

<<<<<<< HEAD
  // Obtener roles actuales del usuario
=======
>>>>>>> qa
  const rolesRes = await fetch(`${baseRolesUrl}/user/${user.id}`);
  const roles = await rolesRes.json();

  if (roles.length > 0) {
    currentRoleId = roles[0].id;
    rolesDiv.innerHTML = `
      <div class="alert alert-info">Rol actual: <strong>${roles[0].name}</strong></div>
    `;
  } else {
    currentRoleId = null;
<<<<<<< HEAD
    rolesDiv.innerHTML = `<div class="alert alert-warning">
    Este usuario no tiene un rol asignado.</div>`;
  }

  // Cargar todos los roles disponibles
=======
    rolesDiv.innerHTML = `<div class="alert alert-warning">Este usuario no tiene un rol asignado.</div>`;
  }

>>>>>>> qa
  const allRolesRes = await fetch(`${baseRolesUrl}`);
  const allRoles = await allRolesRes.json();

  allRoles.forEach(role => {
    const option = document.createElement("option");
    option.value = role.id;
    option.textContent = role.name;
    if (role.id === currentRoleId) {
      option.selected = true;
    }
    roleSelect.appendChild(option);
  });
});

<<<<<<< HEAD
// Habilitar botón si se cambia el rol
document.getElementById("role_select").addEventListener("change", () => {
  const selected = parseInt(document.getElementById("role_select").value);
  document.getElementById("updateBtn").disabled = selected === currentRoleId || 
  isNaN(selected);
});

// Actualizar rol
=======
document.getElementById("role_select").addEventListener("change", () => {
  const selected = parseInt(document.getElementById("role_select").value);
  document.getElementById("updateBtn").disabled = selected === currentRoleId || isNaN(selected);
});

>>>>>>> qa
document.getElementById("updateRoleForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const userId = parseInt(document.getElementById("update_user_id").value);
  const newRoleId = parseInt(document.getElementById("role_select").value);
  const updateBtn = document.getElementById("updateBtn");

  if (newRoleId === currentRoleId || isNaN(newRoleId)) return;

<<<<<<< HEAD
  // Eliminar rol anterior del usuario (si existe)
  await fetch(`${baseRolesUrl}/user/${userId}`, { method: "DELETE" });

  // Asignar nuevo rol
=======
  await fetch(`${baseRolesUrl}/user/${userId}`, { method: "DELETE" });

>>>>>>> qa
  const res = await fetch(`${baseRolesUrl}/assign`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ user_id: userId, role_id: newRoleId })
  });

  const data = await res.json();
  alert(data.message || "Rol actualizado");

  updateBtn.disabled = true;
  document.getElementById("searchForm").dispatchEvent(new Event("submit"));
});
