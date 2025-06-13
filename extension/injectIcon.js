const icon = document.createElement("img");
icon.src = chrome.runtime.getURL("assets/siri.gif");
icon.style.cssText = `
  position: fixed;
  bottom: 20px;
  right: 20px;
  width: 50px;
  height: 50px;
  cursor: pointer;
  z-index: 9999;
`;
document.body.appendChild(icon);

icon.addEventListener("click", () => {
  chrome.runtime.sendMessage({ openPopup: true });
});
