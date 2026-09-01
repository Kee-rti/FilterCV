import cv2
import mediapipe as mp
import math
import numpy as np
from overlay_utils import overlay_transparent

def main():
    print("Initializing FilterCV...")
    
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(
        max_num_faces=1,
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    )
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles

    # Load glasses asset (needs to have an alpha channel)
    glasses = cv2.imread('assets/glasses.png', cv2.IMREAD_UNCHANGED)
    if glasses is None:
        print("Warning: Could not load assets/glasses.png")

    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
        
    print("Webcam initialized. Press 'q' to exit.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        results = face_mesh.process(rgb_frame)
        
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                if glasses is not None:
                    h, w, _ = frame.shape
                    
                    # Left eye outer corner (33) and Right eye outer corner (263)
                    left_eye = face_landmarks.landmark[33]
                    right_eye = face_landmarks.landmark[263]
                    
                    # Nose bridge (168) serves as an anchor for the center of the glasses
                    nose = face_landmarks.landmark[168]
                    
                    # Convert to pixel coordinates
                    lx, ly = int(left_eye.x * w), int(left_eye.y * h)
                    rx, ry = int(right_eye.x * w), int(right_eye.y * h)
                    nx, ny = int(nose.x * w), int(nose.y * h)
                    
                    # Calculate angle
                    # Note: We subtract ry and ly because image y-axis goes down
                    angle = math.degrees(math.atan2(ry - ly, rx - lx))
                    
                    # Calculate width based on eye distance
                    eye_dist = math.hypot(rx - lx, ry - ly)
                    glasses_width = int(eye_dist * 2.0)
                    
                    if glasses_width > 0:
                        scale = glasses_width / glasses.shape[1]
                        glasses_height = int(glasses.shape[0] * scale)
                        
                        if glasses_height > 0:
                            # Resize the glasses
                            resized_glasses = cv2.resize(glasses, (glasses_width, glasses_height))
                            
                            # Rotate the glasses
                            M = cv2.getRotationMatrix2D((glasses_width//2, glasses_height//2), angle, 1.0)
                            rotated_glasses = cv2.warpAffine(
                                resized_glasses, M, (glasses_width, glasses_height), 
                                borderMode=cv2.BORDER_CONSTANT, borderValue=(0,0,0,0)
                            )
                            
                            # Center on nose bridge
                            top_left_x = int(nx - glasses_width / 2)
                            top_left_y = int(ny - glasses_height / 2)
                            
                            # Perform alpha blending overlay
                            # Pass max(0) to avoid negative coordinates if face is at screen edge
                            if top_left_x >= 0 and top_left_y >= 0:
                                frame = overlay_transparent(frame, rotated_glasses, top_left_x, top_left_y)
        
        cv2.imshow('FilterCV - Live Feed', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Exiting...")
            break
            
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
