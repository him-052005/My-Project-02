// public/script.js

// Event listener for Start Cube Scan button
document.addEventListener("DOMContentLoaded", () => {
    const startBtn = document.getElementById("startBtn");
    const statusDiv = document.getElementById("status");

    startBtn.addEventListener("click", () => {
        statusDiv.innerText = "Sending scan request...";

        fetch('http://localhost:5000/start-scan', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(res => res.json())
        .then(data => {
            statusDiv.innerText = "Scan started...";
            console.log("✅ Server Response:", data);
        })
        .catch(err => {
            statusDiv.innerText = "❌ Error starting scan.";
            console.error("Error:", err);
        });
    });
});
