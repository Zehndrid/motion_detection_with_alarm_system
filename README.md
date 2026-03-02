
# Motion Detection Alarm System #NOTE: Used an AI to create this README

**Author:** Dan Efraim V. Hernandez  
**Section:** BSCPE 1-4  
**Assignment:** Activity 2 

## Description
This project is a Python-based security camera script that uses a webcam to detect motion. If sustained movement is detected, it triggers a loud audible alarm. 

This repository serves as an exercise in implementing strict coding standards. The original code from the tutorial has been refactored to enforce `snake_case` formatting and highly descriptive variable/function names.

## Features
- Real-time video capture using OpenCV.
- Image differencing and thresholding to isolate movement.
- Built-in motion counter to prevent false alarms from brief glitches.
- Multi-threading so the video feed doesn't freeze when the alarm rings.

## Prerequisites
Before running this script, you need to have Python installed on your system along with the following libraries:

```bash
pip install opencv-python imutils

```

*(Note: This script uses the `winsound` module, which is only compatible with Windows operating systems).*

## How to Run

1. Clone this repository to your local machine.
2. Open your terminal or command prompt in the project folder.
3. Run the following command:

```bash
python motion_alarm_system.py

```

## Controls

Once the video window opens, click on the window to ensure it is selected, then use the following keyboard controls:

* **`t`** - Toggle the alarm system ON or OFF (arms/disarms the motion detection).
* **`q`** - Quit the application safely and turn off the webcam.

## References

This project is based on the tutorial by NeuralNine:

* [Motion Detection Alarm System in Python](https://www.youtube.com/watch?v=QPjPyUJeYYE&t=980s)

