chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {
  if (msg.openPopup) {
    chrome.windows.create({
      url: chrome.runtime.getURL("popup.html"),
      type: "popup",
      width: 420,
      height: 620
    });
  }
});
