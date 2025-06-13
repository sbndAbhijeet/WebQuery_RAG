function formatMarkdownCodeBlocks(text) {
  // Convert triple backticks to HTML code blocks
  return text.replace(/```(?:\w+)?\n([\s\S]*?)```/g, (match, code) => {
    return `<pre class="bg-dark text-light p-2 rounded mt-2"><code>${code.trim()}</code></pre>`;
  }).replace(/\n/g, "<br>"); // Optional: replace other line breaks
}


document.getElementById("askBtn").addEventListener("click", async () => {
  const query = document.getElementById("userQuery").value.trim();
  const chatContainer = document.getElementById("chatContainer");

  if (!query) return; // prevent empty queries

  // Bot animation toggle
  const botImage = document.getElementById("botIcon");
  botImage.src = "assets/siri.gif";

  try {
    const response = await fetch("http://localhost:8000/query", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question: query })
    });

    let data = await response.json();

    // Handle case where server returns a JSON string instead of object
    if (typeof data === "string") {
      try {
        data = JSON.parse(data);
      } catch (e) {
        console.error("❌ Failed to parse JSON string:", e);
        throw new Error("Invalid JSON from server");
      }
    }
    botImage.src = "assets/icon16.png"
    console.log("✅ Data received:", data);

    const answer = data.Answer || "❌ Error fetching or parsing answer.";
    const section = data.Section || "-";
    const subSection = data.Sub_section || "-";
    const url = data.url || "#";
    const code = data.Code;

    const formattedAnswer = formatMarkdownCodeBlocks(answer);

    const codeBlock = code
      ? `<pre class="bg-dark text-light p-2 rounded mt-2"><code>${code}</code></pre>`
      : "";

    chatContainer.innerHTML += `
  <div class="card bg-light text-dark p-2 mb-3">
    <div><strong>Q:</strong> ${query}</div>
    <div><strong>A:</strong> ${formattedAnswer}</div>
    ${codeBlock}
    <div class="small mt-2">
      <strong>Section:</strong> ${section} |
      <strong>Sub-section:</strong> ${subSection} |
      <a href="${url}" target="_blank" class="text-primary">Open Section 🔗</a>
    </div>
  </div>
`;

    chatContainer.scrollTop = chatContainer.scrollHeight;

  } catch (e) {
    console.error("❌ Fetch Error:", e);
    chatContainer.innerHTML += `
      <div class="alert alert-danger p-2 mb-2">❌ Error fetching response from server.</div>
    `;
  } finally {
    // Restore bot UI
    document.getElementById("botIcon").style.display = "inline-block";
    document.getElementById("lottieMotion").style.display = "none";
    document.getElementById("loader").style.display = "none";
  }
});
