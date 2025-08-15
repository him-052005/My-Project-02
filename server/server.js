const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const { spawn } = require('child_process');
const path = require('path');

const app = express();
app.use(cors());
app.use(bodyParser.json());

// API endpoint to start Rubik's Cube scan
app.post('/start-scan', (req, res) => {
    console.log("📢 Received request to start cube scan...");

    // Path to Python executable in virtual environment
    const pythonExePath = path.join(__dirname, '..', '.venv', 'Scripts', 'python.exe');

    // Path to main.py script
    const pythonScriptPath = path.join(__dirname, '..', 'backend', 'main.py');

    // Spawn Python process
    const python = spawn(pythonExePath, [pythonScriptPath], {
        cwd: __dirname
    });

    // Handle standard output from Python
    python.stdout.on('data', (data) => {
        const message = data.toString().trim();
        console.log(`Python: ${message}`);
        // TODO: send messages to frontend in real-time if needed
    });

    // Handle errors from Python
    python.stderr.on('data', (data) => {
        console.error(`Python Error: ${data}`);
    });

    // When Python finishes
    python.on('close', (code) => {
        console.log(`Python process exited with code ${code}`);
    });

    // Send immediate response to browser
    res.json({ message: 'Scan started' });
});

// Start server
app.listen(5000, () => {
    console.log('🚀 Server running on http://localhost:5000');
});
