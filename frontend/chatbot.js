function sendMessage() {
    const input = document.getElementById('user-input');
    const message = input.value.trim();
    if (!message) return;

    appendMessage("You: " + message, "user-message");
    input.value = "";

    fetch('http://127.0.0.1:5000/chat', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ message })
    })
    .then(response => response.json())
    .then(data => {
        appendMessage("Bot: " + data.reply, "bot-message");
        appendQuote(data.quote);
    })
    .catch(error => {
        appendMessage("Bot: Sorry, something went wrong.", "bot-message");
        console.error(error);
    });
}

function appendMessage(message, className) {
    const chatBox = document.getElementById('chat-box');
    const msgElem = document.createElement('div');
    msgElem.textContent = message;
    msgElem.className = className;
    chatBox.appendChild(msgElem);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function appendQuote(quote) {
    const chatBox = document.getElementById('chat-box');
    const quoteElem = document.createElement('div');
    quoteElem.innerHTML = `<b>${quote}</b>`;
    quoteElem.className = "quote-message";
    chatBox.appendChild(quoteElem);
    chatBox.scrollTop = chatBox.scrollHeight;
}

window.onload = function() {
    appendMessage("Bot: I am a motivational bot! What type of motivation would you like today?", "bot-message");
}
