import cv2
import numpy as np
import time

def rotate_face(face, direction):
    """Rotate a single cube face 90 degrees (placeholder)."""
    if direction == 'clockwise':
        return np.rot90(face, -1)
    elif direction == 'counterclockwise':
        return np.rot90(face, 1)
    else:
        return face

def rotate_cube(faces, move):
    """Apply move to cube faces (placeholder)."""
    print(f"Applying move: {move}")
    return faces

def overlay_moves_on_cube(faces, solution):
    """Overlay moves on cube in live OpenCV window."""
    print("\nOverlaying solution moves on cube...")
    moves = solution.split()

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Cannot open webcam for overlay.")
        return

    for move in moves:
        print(f"Move: {move}")

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Overlay move text
            cv2.putText(frame, f"Move: {move}", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

            # Draw a simple arrow as placeholder
            cv2.arrowedLine(frame, (200, 300), (400, 300), (0, 255, 0), 5)

            cv2.imshow("Rubik's Cube Solution Overlay", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('n'):  # Press 'n' for next move
                break
            elif key == ord('q'):
                print("Overlay cancelled.")
                cap.release()
                cv2.destroyAllWindows()
                return

    cap.release()
    cv2.destroyAllWindows()
    print("Overlay complete.")
