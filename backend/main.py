import cv2
import time
import rotate
import kociemba

def scan_cube_face(face_name):
    print(f"\n[Camera] Get ready to show the {face_name} face...")
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Failed to open webcam.")
        return None

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Show instructions on the frame
        cv2.putText(frame, f"Show {face_name} face and press 's'", 
                    (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Rubik's Cube Scanner", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):  # Press 's' to capture
            print(f"{face_name} face captured!")
            captured_frame = frame.copy()
            break
        elif key == ord('q'):
            print("Scan cancelled by user.")
            captured_frame = None
            break

    cap.release()
    cv2.destroyAllWindows()
    return captured_frame

def scan_all_faces():
    face_names = ["Front", "Right", "Back", "Left", "Up", "Down"]
    faces = []
    for name in face_names:
        face_img = scan_cube_face(name)
        if face_img is None:
            return None
        faces.append(face_img)
        time.sleep(0.5)
    return faces

def compute_solution(faces):
    # Placeholder: convert faces to cube state string for real solving
    print("\nAll faces scanned successfully!")
    print("Computing solution...")
    solution = "R L U2 R L' B2 U2 R2 F2 L2 D2 L2 F2"
    print(f"Solution: {solution}")
    return solution

def start_cube_scan():
    print("=== Rubik's Cube Solver Started ===")
    faces = scan_all_faces()
    if faces is None:
        print("Cube scanning failed or cancelled.")
        return

    solution = compute_solution(faces)
    print("\nStarting augmented reality overlay of moves...")
    rotate.overlay_moves_on_cube(faces, solution)

if __name__ == "__main__":
    start_cube_scan()
