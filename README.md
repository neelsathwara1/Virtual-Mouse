# Virtual-Mouse
This project implements a Virtual Mouse using computer vision techniques, powered by OpenCV and machine learning/deep learning models. The virtual mouse enables users to control the mouse pointer using hand gestures or head movements, eliminating the need for physical hardware.

## Features
- Hand Gesture Recognition: Detect and recognize hand gestures to perform mouse actions such as moving the cursor, clicking, dragging, and scrolling.
- Object Detection and Tracking: Efficient hand detection using machine learning or deep learning models.
- Customizable Gestures: Supports custom gesture configurations for different mouse actions.
- Smooth Cursor Control: Achieves smooth and responsive cursor movement using real-time video input from the webcam.
= Platform Independence: Runs on any platform that supports Python and OpenCV, such as Windows, macOS, and Linux.

## Technologies Used
OpenCV: For real-time computer vision and video processing.
Machine Learning (ML): Hand detection and gesture classification models.
Deep Learning (DL): Optionally integrates more advanced models like CNNs for more robust detection.
Mediapipe : Google’s hand tracking library for robust hand landmark detection.

## Prerequisites
To run this project, you will need:
Python 3.x
OpenCV
NumPy
TensorFlow / Keras (for DL models)
Mediapipe 

## How It Works
1. The webcam captures real-time video input.
2. OpenCV processes the frames to detect and track hand movements or gestures.
3. A pre-trained ML/DL model classifies the hand gestures (e.g., finger positions) and maps them to specific mouse actions.
4. The virtual mouse moves the cursor, performs clicks, drags, or other actions based on the recognized gestures.
