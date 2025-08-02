const form = document.getElementById('chat-form');
const input = document.getElementById('user-input');
const messages = document.getElementById('messages');
const endBtn = document.getElementById('end-btn');

const END_WORDS = ["bye", "exit", "quit", "goodbye", "see you", "farewell"];
let ended = false;

function appendMessage(text, sender) {
    const msg = document.createElement('div');
    msg.className = 'msg ' + sender;
    msg.textContent = text;
    messages.appendChild(msg);
    messages.scrollTop = messages.scrollHeight;
}

function endConversation() {
    ended = true;
    appendMessage("🌼 It was lovely talking to you. You're never alone. Take care. 💛", "maya");
    input.disabled = true;
    endBtn.disabled = true;
}

form.onsubmit = async (e) => {
    e.preventDefault();
    if (ended) return;
    const text = input.value.trim();
    if (!text) return;
    appendMessage(text, 'user');
    input.value = '';
    messages.scrollTop = messages.scrollHeight;
    // Smart end detection
    if (END_WORDS.some(word => text.toLowerCase().includes(word))) {
        endConversation();
        return;
    }
    try {
        const res = await fetch('/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: text })
        });
        const data = await res.json();
        appendMessage(data.response || data.error || 'Error', 'maya');
    } catch (err) {
        appendMessage('Error connecting to Maya.', 'maya');
    }
};

endBtn.onclick = () => {
    if (!ended) endConversation();
};
