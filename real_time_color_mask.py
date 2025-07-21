# -*- coding: utf-8 -*-
"""
Performs real-time color detection and masking on a webcam feed using OpenCV.

This script captures video from the default webcam, isolates pixels within a
specified color range (blue, by default), applies this mask to the video,
and displays both the original and masked feeds. The masked video is also
saved to a file named 'video_with_mask.avi'.

Dependencies:
    - opencv-python
    - numpy

Usage:
    Run the script. Two windows will appear showing the webcam feed.
    Press the 'q' key to stop the script and save the video.
"""

import cv2
import numpy as np

# --- CONFIGURATION ---
# Define the color range for the mask (HSV color space).
# This example is for detecting the color blue.
LOWER_COLOR_BOUND = np.array([100, 150, 0])
UPPER_COLOR_BOUND = np.array([140, 255, 255])
OUTPUT_FILENAME = 'video_with_mask.avi'

# --- INITIALIZATION ---
# Capture video from the default webcam (index 0).
webcam_capture = cv2.VideoCapture(0)

# Verify that the webcam opened correctly.
if not webcam_capture.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Get video properties (width, height, fps) for the output file.
frame_width = int(webcam_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(webcam_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(webcam_capture.get(cv2.CAP_PROP_FPS))

# If FPS is 0, use a default value (e.g., 20 or 30).
if fps == 0:
    fps = 20
    print(f"Warning: Could not get webcam FPS. Defaulting to {fps} FPS.")

# Define the codec and create the VideoWriter object to save the video.
fourcc_codec = cv2.VideoWriter_fourcc(*'XVID')
video_writer = cv2.VideoWriter(OUTPUT_FILENAME, fourcc_codec, fps, (frame_width, frame_height))

print("Starting webcam feed... Press 'q' to quit.")

# --- MAIN LOOP ---
while True:
    # Read a single frame from the webcam feed.
    is_successful, frame = webcam_capture.read()
    if not is_successful:
        print("Stream ended or failed to read frame.")
        break

    # Convert the frame from the BGR color space to HSV.
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask that isolates pixels within the defined color range.
    color_mask = cv2.inRange(hsv_frame, LOWER_COLOR_BOUND, UPPER_COLOR_BOUND)

    # Apply the mask to the original frame using a bitwise AND operation.
    # This keeps only the pixels where the mask is non-zero (i.e., the blue pixels).
    masked_frame = cv2.bitwise_and(frame, frame, mask=color_mask)

    # Display the original and the masked frames in separate windows.
    cv2.imshow('Original Webcam Feed', frame)
    cv2.imshow('Masked Feed', masked_frame)

    # Write the frame with the mask applied to the output video file.
    video_writer.write(masked_frame)

    # Exit the loop if the 'q' key is pressed.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# --- CLEANUP ---
# Release all resources.
print("Exiting and releasing resources...")
webcam_capture.release()
video_writer.release()
cv2.destroyAllWindows()