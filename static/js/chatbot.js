document.addEventListener("DOMContentLoaded", function () {
  const chatToggle = document.getElementById("chatToggle");
  const chatBox = document.getElementById("chatBox");
  const chatMessages = document.getElementById("chatMessages");
  const chatInput = document.getElementById("chatInput");

  // Mostrar bienvenida automática al cargar


  chatToggle.addEventListener("click", () => {
    chatBox.classList.toggle("d-none");
  });

  chatInput.addEventListener("keypress", function (e) {
    if (e.key === "Enter") {
      const userMsg = chatInput.value.trim();
      if (userMsg) {
        addMessage("Tú", userMsg);
        chatInput.value = "";
        setTimeout(() => {
          botReply(userMsg);
        }, 500);
      }
    }
  });


//#esta función agrega un mensaje al chat con el formato adecuado y hace scroll hacia abajo para mostrar el último mensaje
function addMessage(sender, text) {
  const msg = document.createElement("div");
  msg.classList.add("mb-2", "chat-message");
  msg.innerHTML = `<strong>${sender}:</strong> ${text}`;
  chatMessages.appendChild(msg);
  chatMessages.scrollTop = chatMessages.scrollHeight;
}



  //#está función simula respuestas del bot según palabras clave en el mensaje del usuario

function botReply(userMsg) {
  let reply = "Lo siento, no entendí tu consulta.";

  if (userMsg.toLowerCase().includes("dirección")) {
    reply = "📍 Estamos ubicados en Esmeraldas, Ecuador, Av. Principal #123.";
  } else if (userMsg.toLowerCase().includes("horario")) {
    reply = "🕘 Nuestro horario es de lunes a viernes de 9:00 a 18:00.";
  } else if (userMsg.toLowerCase().includes("servicio")) {
    reply = "🦷 Ofrecemos odontología general, ortodoncia, estética dental y más.";
  } else if (userMsg.toLowerCase().includes("contacto") || userMsg.toLowerCase().includes("contactar")) {
    reply = `
      📞 Teléfono: 099-485-3308  
      💬 WhatsApp: <a href="https://wa.me/593994853308" target="_blank">Escríbenos aquí</a>  
      📧 Correo: <a href="mailto:clinicatatiana@gmail.com">clinicatatiana@gmail.com</a>
    `;
  }

  addMessage("Asistente", reply);
}



//#esta función muestra opciones rápidas para que el usuario pueda hacer clic y obtener respuestas predefinidas

function showQuickOptions() {
  const options = document.createElement("div");
  options.classList.add("quick-options", "mt-3");

  options.innerHTML = `
    <button class="btn btn-outline-primary btn-sm me-2">Ver horarios</button>
    <button class="btn btn-outline-success btn-sm me-2">Ver servicios</button>
    <button class="btn btn-outline-info btn-sm">Contactar</button>
  `;

  chatMessages.appendChild(options);

  // Eventos de los botones
  options.querySelectorAll("button").forEach(btn => {
    btn.addEventListener("click", () => {
      const text = btn.innerText;
      addMessage("Tú", text);
      botReply(text);
    });
  });
}

// Mostrar bienvenida + opciones al cargar
setTimeout(() => {
  chatBox.classList.remove("d-none");
  addMessage("Asistente", "👋 Hola, soy tu asistente virtual de la Clínica Dental Tatiana Maldonado. Puedo ayudarte con preguntas sobre dirección, horarios, servicios y más.");
  showQuickOptions();
}, 1000);
});




