const askBtn = document.getElementById("askBtn");
const queryInput = document.getElementById("userQuery");
const chatContainer = document.getElementById("chatContainer");
const loader = document.getElementById("loader");
const botIcon = document.getElementById("botIcon");
const lottieMotion = document.getElementById("lottieMotion");

lottieMotion.style.display = "none";

let chatHistory = [];

function renderChat() {
  chatContainer.innerHTML = ""; // Clear before rendering

  chatHistory.forEach(({ question, answerObj }) => {
    // User Message
    const userMsg = document.createElement("div");
    userMsg.className = "message user";
    userMsg.innerText = question;
    chatContainer.appendChild(userMsg);

    // Bot Message
    const botMsg = document.createElement("div");
    botMsg.className = "message bot";
    botMsg.innerHTML = `
      <b>Answer:</b> ${answerObj.Answer}<br>
      <b>Section:</b> ${answerObj.Section}<br>
      <b>Sub-section:</b> ${answerObj["Sub-section"]}<br>
      <b>URL:</b> <a href="${answerObj.url}" target="_blank">${answerObj.url}</a>
    `;
    chatContainer.appendChild(botMsg);
  });

  chatContainer.scrollTop = chatContainer.scrollHeight;
}

askBtn.addEventListener("click", async () => {
  const query = queryInput.value.trim();
  if (!query) return;

  queryInput.value = "";

  // Show animation
  botIcon.style.display = "none";
  lottieMotion.style.display = "block";
  loader.style.display = "block";

  try {
    const response = await fetch("http://localhost:8000/query", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query })
    });

    const data = await response.json();
    let raw = data.answer.trim();
    if (raw.startsWith("```json")) {
      raw = raw.replace(/^```json\s*/, "").replace(/\s*```$/, "");
    }

    const parsed = JSON.parse(raw);

    // Save into memory
    chatHistory.push({
      question: query,
      answerObj: parsed
    });

    renderChat();
  } catch (e) {
    chatHistory.push({
      question: query,
      answerObj: {
        Answer: "❌ Error fetching or parsing answer.",
        Section: "-",
        "Sub-section": "-",
        url: "#"
      }
    });

    renderChat();
    console.error(e);
  } finally {
    loader.style.display = "none";
    lottieMotion.style.display = "none";
    botIcon.style.display = "block";
  }
});
