<div align="center">

# 📷 OpenCV Real-Time Color Detection

**A computer vision script for real-time color masking using a webcam**

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](#)
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](#)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](#)

*A Python-based utility that utilizes OpenCV to capture live video feeds and apply HSV color space thresholding to detect, mask, and isolate specific colors in real-time.*

</div>

<br />

## 📑 Table of Contents
- [✨ Key Features](#-key-features)
- [🏗️ Architecture & Structure](#️-architecture--structure)
- [🚀 Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Execution](#execution)
- [🛠️ Tech Stack](#️-tech-stack)

---

## ✨ Key Features

* **✔️ Live Video Feed:** Captures and processes real-time video directly from your system's default webcam.
* **✔️ HSV Color Masking:** Converts standard BGR video frames into the HSV (Hue, Saturation, Value) color space for highly accurate and robust color detection.
* **✔️ Real-time Filtering:** Applies binary masking (thresholding) to isolate specific color ranges dynamically as the video plays.
* **✔️ Multi-Window Visualization:** Simultaneously displays the original live feed, the generated binary mask, and the final color-filtered result for easy debugging and demonstration.

---

## 🏗️ Architecture & Structure

The repository is kept simple and focused on the core computer vision logic:

```text
opencv-real-time-color-detection/
├── real_time_color_mask.py      # Main webcam tracking and color masking script
└── README.md                    # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

To run this script, ensure you have Python installed on your local machine along with the required computer vision and matrix calculation libraries:

* **Python:** Version 3.x
* **OpenCV:** For video capture and image processing (`cv2`)
* **NumPy:** For advanced array and matrix operations (`numpy`)
* **Hardware:** A functional webcam connected to your machine.

You can install the required dependencies using pip:
```bash
pip install opencv-python numpy
```

### Execution

1. Clone this repository to your local machine:
   ```bash
   git clone <your-repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd opencv-real-time-color-detection
   ```
3. Run the Python script:
   ```bash
   python real_time_color_mask.py
   ```
4. A window will open utilizing your webcam. Hold up a colored object (matching the HSV range specified in the code) to see the mask tracking it in real-time.
5. Press `q` on your keyboard to stop the execution and close the windows.

---

## 🛠️ Tech Stack

* **Python** - Core programming language
* **OpenCV (`cv2`)** - Computer Vision, video capture, and color space conversion
* **NumPy (`np`)** - Matrix operations for defining HSV lower and upper bounds

<br />

<div align="center">
  <i>Developed with ☕ to explore Computer Vision and Real-Time Processing.</i>
</div>
