// Frontend JavaScript per l'interfaccia della chat
async function sendMessage(message) {
    // Mostra il messaggio dell'utente
    const chatBox = document.getElementById('chat-box');
    chatBox.innerHTML += `<div class="user-message">${message}</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;
    
    // Invia la richiesta al backend
    try {
        const response = await fetch('http://localhost:8000/ollama', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: `message=${encodeURIComponent(message)}`
        });
        
        if (response.ok) {
            const data = await response.json();
            chatBox.innerHTML += `<div class="ai-message">${data.message}</div>`;
            chatBox.scrollTop = chatBox.scrollHeight;
        } else {
            throw new Error('Errore nella richiesta');
        }
    } catch (error) {
        chatBox.innerHTML += `<div class="error-message">${error.message}</div>`;
        chatBox.scrollTop = chatBox.scrollHeight;
    }
}

document.getElementById('message-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const message = document.getElementById('message-input').value.trim();
    if (message) {
        sendMessage(message);
        document.getElementById('message-input').value = '';
    }
});
