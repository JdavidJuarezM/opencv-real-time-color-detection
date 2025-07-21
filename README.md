# Opencv-real-time-color-detection
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
