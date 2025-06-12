document.getElementById("askBtn").addEventListener("click", async () => {
  const query = document.getElementById("userQuery").value;
  const answerDiv = document.getElementById("answer");
  answerDiv.innerText = "Thinking...";

  try {
    const response = await fetch("http://localhost:8000/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query })
    });

    const data = await response.json();
    answerDiv.innerHTML = `<b>Answer:</b> ${data.answer || JSON.stringify(data)}`;
  } catch (e) {
    answerDiv.innerText = "Error fetching answer. Is the backend running?";
  }
});
