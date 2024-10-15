// Funkce pro spuštění ping floodu
function startFlood() {
    const targetIp = document.getElementById("target_ip").value;
    const countdownSeconds = document.getElementById("countdown_seconds").value;

    fetch('http://localhost:5000/api/start_flood', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            target_ip: targetIp,
            countdown_seconds: countdownSeconds
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("message").innerText = data.message;
        document.getElementById("stop_flood").style.display = "block";
        document.getElementById("stop_flood").setAttribute('data-thread-id', data.thread_id);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

// Funkce pro zastavení ping floodu
function stopFlood() {
    const threadId = document.getElementById("stop_flood").getAttribute('data-thread-id');

    fetch(`http://localhost:5000/api/stop_flood/${threadId}`, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("message").innerText = data.message;
        document.getElementById("stop_flood").style.display = "none";
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}