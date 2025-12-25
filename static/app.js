const messagesEl = document.getElementById("messages");
const inputEl = document.getElementById("input");
const sendBtn = document.getElementById("send");

function addMessage(role, text) {
  const div = document.createElement("div");
  div.className = `message ${role}`;
  div.innerHTML = `<strong>${role.toUpperCase()}:</strong> ${text}`;
  messagesEl.appendChild(div);
  messagesEl.scrollTop = messagesEl.scrollHeight;
}

sendBtn.onclick = async () => {
  const text = inputEl.value.trim();
  if (!text) return;

  // Show user message
  addMessage("user", text);
  inputEl.value = "";

  try {
    const res = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text })
    });

    const data = await res.json();
    addMessage("assistant", data.reply || "Error occurred");
  } catch (err) {
    addMessage("assistant", "Error: could not connect to server.");
  }
};