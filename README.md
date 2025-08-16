<h1 align="center">🧩 ViziCube – Rubik’s Cube Solver</h1>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.11-blue" alt="Python"></a>
  <a href="https://opencv.org/"><img src="https://img.shields.io/badge/OpenCV-4.x-brightgreen" alt="OpenCV"></a>
  <a href="https://pypi.org/project/kociemba/"><img src="https://img.shields.io/badge/kociemba-1.2.1-orange" alt="kociemba"></a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript"><img src="https://img.shields.io/badge/JavaScript-ES6-yellow" alt="JavaScript"></a>
  <a href="https://nodejs.org/"><img src="https://img.shields.io/badge/Node.js-LTS-green" alt="Node.js"></a>
  <a href="https://expressjs.com/"><img src="https://img.shields.io/badge/Express-4.x-lightblue" alt="Express"></a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5"><img src="https://img.shields.io/badge/HTML5-red" alt="HTML5"></a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/CSS"><img src="https://img.shields.io/badge/CSS3-blueviolet" alt="CSS3"></a>
</p>

<p align="center">
  <em>Scan your physical Rubik’s Cube, compute the solution, and follow step-by-step moves in augmented reality with ViziCube – your virtual cube master!</em>
</p>

---

<h2>🎯 Quick Features</h2>

<ul>
  <li>📷 <b>Guided Cube Scanning</b> – Capture all six cube faces at your pace</li>
  <li>🧠 <b>Optimal Solution Computation</b> – Uses the kociemba algorithm for the shortest sequence of moves</li>
  <li>✨ <b>Augmented Reality Overlay</b> – Step-by-step arrows and instructions directly on the webcam feed</li>
  <li>⏩ <b>Step Control</b> – Press 'n' for next move, 'q' to quit overlay</li>
  <li>✅ <b>Immediate Feedback</b> – Displays which face to scan next and confirms capture</li>
</ul>

---

<h2>🚀 How ViziCube Works</h2>

<ol>
  <li>Open the interface – A modern webpage with a <b>Start Cube Scan</b> button loads.</li>
  <li>Start the scan – Click the button to launch the cube solver.</li>
  <li>Show your cube – Follow webcam prompts to capture:
    <ul>
      <li>Front face first, press <code>s</code> to capture</li>
      <li>Repeat for Right, Back, Left, Up, and Down faces</li>
      <li>Press <code>q</code> anytime to cancel</li>
    </ul>
  </li>
  <li>Compute the solution – ViziCube calculates the optimal sequence of moves.</li>
  <li>Augmented Reality overlay – Step-by-step moves appear live on the webcam feed.</li>
</ol>

---

<h2>🛠️ Tech Stack</h2>

<table>
  <tr>
    <td>Python 3.11</td>
    <td>Core logic and cube-solving algorithms</td>
  </tr>
  <tr>
    <td>OpenCV 4.x</td>
    <td>Webcam capture, image processing, and AR overlays</td>
  </tr>
  <tr>
    <td>kociemba 1.2.1</td>
    <td>Computes optimal Rubik’s Cube solutions</td>
  </tr>
  <tr>
    <td>JavaScript ES6 & Node.js 20.x</td>
    <td>Frontend-backend communication, interface logic</td>
  </tr>
  <tr>
    <td>Express 4.x</td>
    <td>Handles scan requests and server logic</td>
  </tr>
  <tr>
    <td>HTML5 & CSS3</td>
    <td>Responsive and modern UI for user interaction</td>
  </tr>
</table>

---

<h2>🎮 How to Use</h2>

<ol>
  <li>Open the interface in your browser.</li>
  <li>Click <b>Start Cube Scan</b>.</li>
  <li>Follow webcam instructions to capture all six cube faces.</li>
  <li>Watch the AR overlay guide you step by step to solve your cube!</li>
</ol>

---

<h2>⚡ Highlights</h2>

<ul>
  <li>Interactive and user-friendly interface</li>
  <li>Real-time AR overlay with live arrows and instructions</li>
  <li>Step-by-step control using keyboard commands</li>
  <li>Optimized for physical cube scanning and solving</li>
</ul>

---

<h2>💡 Future Enhancements</h2>

<ul>
  <li>Automatic color detection for accurate cube solving 🎨</li>
  <li>Exact rotation arrows per face 🔄</li>
  <li>Real-time streaming of instructions to the interface 🌐</li>
  <li>Mobile-friendly scanning via phone camera 📱</li>
</ul>

<h2>🎉 Demo / Screenshots</h2>

<p align="center">
  <!-- Image Example -->
  <img src="server.js running.png" alt="server.js running" width="400">
</p>

<p align="center">
  <!-- Video Example -->
  <video width="600" controls>
    <source src="live server running.mp4" type="video/mp4">
  </video>
</p>

<p align="center">
  <!-- Image Example -->
  <img src="suggesting moves.png" alt="suggesting moves" width="400">
</p>
