🧩 Rubik’s Cube Solver

Welcome to the Rubik’s Cube Solver! This project lets you scan your physical Rubik’s Cube using your webcam, compute the solution, and see step-by-step moves in augmented reality. It’s like having a virtual cube master guiding you live!

🎯 What It Does
Staring at a scrambled cube and feeling stuck? This project solves it for you:

Scan: Captures all six faces of your cube using the webcam.

Compute: Calculates the optimal sequence of moves to solve the cube.

Visualize: Displays arrows and move instructions directly on the live video feed.

All you have to do is show your cube to the camera, press a button, and follow along.

🚀 How It Works

Here’s the interactive flow:

Open the interface
You’ll see a clean page with a “Start Cube Scan” button.

Start the scan
Click the button to launch the cube solver.

Show your cube
The webcam opens and gives instructions:

[Camera] Get ready to show the Front face...

Press ‘s’ to capture each face.

Repeat for Right, Back, Left, Up, and Down faces.

Press ‘q’ anytime to cancel.

Compute the solution
After all six faces are captured, the program calculates the solution.

Augmented reality overlay
The webcam shows step-by-step moves with arrows and instructions:

Press ‘n’ to go to the next move.

Press ‘q’ to quit the overlay.

Now you can follow the moves on your cube as if a virtual cube master is guiding you live!

🖥️ Interactive Features

Guided scanning: Captures faces only when you’re ready.

Live AR overlay: Moves appear directly on the video feed.

Step-by-step instructions: Control the pace with keyboard commands.

Immediate feedback: Shows which face to scan next and confirms capture.

🛠️ Technologies Used

Python: Computer vision and AR overlay

OpenCV: Webcam capture and drawing arrows on video

Cube solving algorithm: Computes optimal moves

JavaScript / Node.js: Runs backend and connects interface with Python

Frontend: Clean, modern interface with buttons and status messages

🎮 How to Use
Open the interface in your browser.

Click Start Cube Scan.

Follow webcam instructions to capture all six cube faces.

Watch the AR overlay guide you step by step to solve your cube!

⚡ Highlights
Interactive and user-friendly.

Augmented reality overlay with live arrows and instructions.

Step-by-step control using keyboard commands.

Works in real-time with your physical cube.

💡 Future Improvements
Detect cube colors automatically for accurate solving.

Show exact rotation arrows per face.

Stream instructions to the interface in real-time.

Mobile-friendly scanning via phone camera.

🎉 Summary

This project is an interactive Rubik’s Cube experience, combining computer vision, cube-solving logic, and live AR visualization. Just show your cube, follow the steps, and solve it like a pro!
