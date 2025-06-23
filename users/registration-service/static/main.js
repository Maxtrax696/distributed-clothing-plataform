const emailInput = document.getElementById("email");
const phoneInput = document.getElementById("phone_number");
const passwordInput = document.getElementById("password");
const submitBtn = document.getElementById("submitBtn");
const feedback = document.getElementById("email-feedback");
const form = document.getElementById("registerForm");
const result = document.getElementById("message");

let emailIsValid = false;

<<<<<<< HEAD
// Validar si el email ya existe
=======
>>>>>>> qa
emailInput.addEventListener("blur", async () => {
  const username = emailInput.value.trim();
  const fullEmail = username + "@flakos.com";

  if (username.length === 0) {
    feedback.innerText = "";
    submitBtn.disabled = true;
<<<<<<< HEAD
    emailIsValid = false;
    return;
  }

  try {
    const res = await fetch(`/api/register/check-email?email=${encodeURIComponent(fullEmail)}`);
    const data = await res.json();

    if (data.exists) {
      feedback.innerHTML = `<span class="text-danger">❌ El correo ya está registrado</span>`;
      emailIsValid = false;
      submitBtn.disabled = true;
    } else {
      feedback.innerHTML = `<span class="text-success">✔ Correo disponible</span>`;
      emailIsValid = true;
      submitBtn.disabled = false;
    }
  } catch (error) {
    feedback.innerHTML = `<span class="text-danger">⚠ Error al verificar el correo</span>`;
    emailIsValid = false;
    submitBtn.disabled = true;
  }
});

// Evento de envío del formulario
form.addEventListener("submit", async (e) => {
  e.preventDefault();

  if (!emailIsValid) {
    result.innerHTML = `<div class="alert alert-danger">❌ Verifica que el correo sea válido</div>`;
    return;
  }

  const username = emailInput.value.trim();
  const fullEmail = username + "@flakos.com";
  const phone = phoneInput.value;
  const password = passwordInput.value;

  // Validación de teléfono: debe ser 8 dígitos y se antepone 09
  if (!/^\d{8}$/.test(phone)) {
    result.innerHTML = `<div class="alert alert-danger">📵 Ingresa los 8 dígitos restantes del teléfono (comienza con 09)</div>`;
    return;
  }

  // Validación de contraseña
  const passwordRegex = /^(?=.*[A-Z])(?=.*[!@#$%^&*()_+\-=[\]{};':"\\|,.<>/?]).{8,}$/;
  if (!passwordRegex.test(password)) {
    result.innerHTML = `<div class="alert alert-danger">🔐 La contraseña debe tener mínimo 8 caracteres, una mayúscula y un símbolo</div>`;
    return;
  }

  // Datos a enviar
=======
    return;
  }

  const res = await fetch(`/api/register/check-email?email=${encodeURIComponent(fullEmail)}`);
  const data = await res.json();

  if (data.exists) {
    feedback.innerHTML = `<span class="text-danger">❌ El correo ya está registrado</span>`;
    emailIsValid = false;
    submitBtn.disabled = true;
  } else {
    feedback.innerHTML = `<span class="text-success">✔ Correo disponible</span>`;
    emailIsValid = true;
    submitBtn.disabled = false;
  }
});

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  if (!emailIsValid) return;

  const fullEmail = emailInput.value.trim() + "@flakos.com";
  const phone = phoneInput.value;
  const password = passwordInput.value;

  if (!/^\d{8}$/.test(phone)) {
    result.innerHTML = `<div class="alert alert-danger">📵 Teléfono debe tener 10 dígitos empezando por 09</div>`;
    return;
  }

  const passwordRegex = /^(?=.*[A-Z])(?=.*[!@#$%^&*()_+\-=[\]{};':"\\|,.<>/?]).{8,}$/;
  if (!passwordRegex.test(password)) {
    result.innerHTML = `<div class="alert alert-danger">🔐 Contraseña débil: 8+ caracteres, 1 mayúscula y símbolo</div>`;
    return;
  }

>>>>>>> qa
  const data = {
    first_name: document.getElementById("first_name").value,
    last_name: document.getElementById("last_name").value,
    birth_date: document.getElementById("birth_date").value,
    email: fullEmail,
    password: password,
    phone_number: "09" + phone
  };

<<<<<<< HEAD
  // Enviar a backend
  const response = await fetch("/api/register", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
=======
  const response = await fetch("/api/register", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
>>>>>>> qa
  });

  const resData = await response.json();

  if (response.ok) {
    result.innerHTML = `<div class="alert alert-success">${resData.message}</div>`;
    form.reset();
    feedback.innerHTML = "";
    emailIsValid = false;
    submitBtn.disabled = true;
    document.getElementById("first_name").focus();
  } else {
    result.innerHTML = `<div class="alert alert-danger">❌ ${resData.detail}</div>`;
  }
});
