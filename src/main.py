import cv2

def main():
    print("Initializing FilterCV...")
    
    # Initialize video capture (0 is usually the default webcam)
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
        
    print("Webcam initialized. Press 'q' to exit.")
    
    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Failed to grab frame.")
            break
            
        # Flip the frame horizontally for a mirror effect
        frame = cv2.flip(frame, 1)
        
        # Display the frame
        cv2.imshow('FilterCV - Live Feed', frame)
        
        # Wait for 1 ms and check if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Exiting...")
            break
            
    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
