import cv2
import numpy as np
import threading
import playsound
import time

# Global variables
Alarm_Status = False
last_fire_detected_time = 0  
alarm_thread = None

# Function to play alarm sound
def play_alarm_sound():
    playsound.playsound('sound1.mp3', True)             

# Function to stop the alarm sound (to avoid continuous playing)
def stop_alarm():
    global alarm_thread
    if alarm_thread is not None:
        alarm_thread._stop()  # Stop the alarm thread manually
        alarm_thread = None
                            
# Main program
def fire_detection():
    global Alarm_Status, last_fire_detected_time, alarm_thread

    # Open webcam
    video = cv2.VideoCapture(0)

    if not video.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        # Capture frame from webcam
        ret, frame = video.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Resize frame for better processing
        frame = cv2.resize(frame, (960, 540))

        # Apply Gaussian Blur
        blur = cv2.GaussianBlur(frame, (21, 21), 0)

        # Convert frame to HSV color space
        hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

        # Define HSV range for detecting fire-like colors
        lower = np.array([18, 50, 50], dtype="uint8")
        upper = np.array([35, 255, 255], dtype="uint8")

        # Create mask to detect fire colors
        mask = cv2.inRange(hsv, lower, upper)

        # Highlight fire regions in the frame
        output = cv2.bitwise_and(frame, frame, mask=mask)

        # Count the number of fire-like pixels
        fire_pixels = cv2.countNonZero(mask)

        # Fire detection threshold
        fire_threshold = 15000  # Can be adjusted based on testing and webcam resolution
      
        # Fire detected logic
        if fire_pixels > fire_threshold:
            print("Fire detected!")
            last_fire_detected_time = time.time()

            if not Alarm_Status:
                Alarm_Status = True
                alarm_thread = threading.Thread(target=play_alarm_sound)
                alarm_thread.start()

        # If no fire detected for a certain time, stop the alarm
        elif Alarm_Status and (time.time() - last_fire_detected_time > 5):  # No fire detected for 5 seconds
            print("No fire detected. Stopping alarm.")
            Alarm_Status = False
            stop_alarm()

        # Display the original frame and output
        cv2.imshow("Webcam Feed", frame)
        cv2.imshow("Fire Detection", output)

        # Exit when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    video.release()
    cv2.destroyAllWindows()

# Run the fire detection function
if __name__ == "__main__":
    fire_detection()
