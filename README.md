# Fire-Detection-System

---

# Fire Detection System Using OpenCV

This project detects fire-like colors from a webcam feed using OpenCV and triggers an alarm if a fire is detected. The system processes the video stream, identifies fire-like colors, and alerts the user with an alarm sound when a fire is detected. If no fire is detected within a specified time frame, the alarm will stop automatically.

---

## Features

* **Webcam - based fire detection** : Uses the webcam to capture frames and analyze them for fire-like colors (typically orange/red hues).
* **Alarm System** : When a fire is detected, an alarm sound is played. The alarm stops if no fire is detected for a certain period.
* **Real - time Video Feed** : Displays both the original webcam feed and a filtered feed showing only fire-like regions.

---

## Requirements

Before running the project, make sure you have the following installed :

* Python 3.x
* OpenCV (`cv2`)
* Numpy
* `playsound` library

To install the required Python libraries, use the following commands :

```bash
pip install opencv-python numpy playsound
```

---

## How It Works

1. **Capture Webcam Feed** : The program starts by opening the webcam and capturing frames.
2. **Frame Preprocessing** : Each frame is resized, blurred, and converted to the HSV (Hue, Saturation, Value) color space.
3. **Fire Color Detection** : The system uses a predefined HSV color range to detect pixels that match fire-like colors (typically yellow-red-orange).
4. **Alarm Trigger** : If the number of fire-like pixels exceeds a defined threshold, the alarm is triggered by playing an MP3 sound file.
5. **Alarm Stop** : If no fire is detected within 5 seconds, the alarm is stopped.

---

## Setup Instructions

### 1. Clone the Repository

Clone this repository to your local machine using the following command :

```bash
git clone https://github.com/yourusername/fire-detection.git
cd Fire-Detection-System
```

### 2. Add Alarm Sound

Download an alarm sound (e.g., `sound1.mp3`) and place it in the project directory. This sound file will be played when fire is detected.

### 3. Run the Program

After setting up, run the program with the following command :

```bash
Fire Detection System.py
```

### 4. Exit the Program

Press the `q` key to quit the program.

---

## Code Overview

### Key Functions

* **`play_alarm_sound()`** : Plays the alarm sound when fire is detected.
* **`stop_alarm()`** : Stops the alarm when no fire is detected for 5 seconds.
* **`fire_detection()`** : Main function that captures webcam frames, processes them, detects fire, and handles alarm logic.

### Fire Detection Logic

* **HSV Thresholding** : The system looks for fire-like colors by filtering pixels in the HSV color space within a defined range.
* **Fire Pixel Count** : If the number of pixels matching the fire color exceeds the threshold (`fire_threshold`), it triggers the alarm.

### Alarm Timing

* **Alarm Duration** : The alarm will keep playing as long as fire is detected. Once no fire is detected for 5 seconds, the alarm will stop.

---

## Customization

* **Threshold Adjustments** : You can adjust the `fire_threshold` value to make the system more or less sensitive to fire detection based on your environment.
* **HSV Range** : The HSV range for detecting fire-like colors can also be adjusted if you notice the system isn't detecting fire correctly.

---

## Known Issues

* The system may give false positives or miss detections based on lighting conditions, camera quality, and fire color accuracy.
* The alarm sound might not stop immediately due to threading issues with `playsound`.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contributing

Feel free to fork the repository, open issues, and submit pull requests. If you make improvements or fixes, your contributions are welcome!

---

## Contact

If you have any questions or suggestions, feel free to open an issue on GitHub.

---
