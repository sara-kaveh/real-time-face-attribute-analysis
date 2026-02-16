# Real-Time Face Attribute Analysis

**Real-Time Face Attribute Analysis using OpenCV and DeepFace**  
Detects **emotion, age, gender and race** from webcam in real time.

---

## Features

- Detect faces using OpenCV Haar Cascade
- Predict facial **emotion, age, gender, and race** using DeepFace
- Supports **multiple faces simultaneously**
- Real-time display with bounding boxes and labels
- Modular code structure for easy maintenance and extension
- Performance optimizations for smoother real-time execution
- Press **S** during the live webcam feed to save a screenshot
- Screenshots are saved in the project directory with unique filenames

---

## How It Works

1. Webcam captures video frames
2. OpenCV detects faces
3. DeepFace analyzes each detected face
4. Results displayed in real time with labels

---

## Technologies

- Python 3.10+  
- OpenCV — Video capture & face detection
- DeepFace — Face attribute analysis
- TensorFlow — DeepFace backend
- NumPy — Numerical operations

---

## Performance Optimizations

To improve real-time performance and reduce CPU usage:
- Face analysis runs every 10 frames instead of every frame
- Frames are resized to 50% before analysis for faster processing
- Uses Haar Cascade for fast real-time detection
- Improves responsiveness and reduces lag
  
---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/sara-kaveh/real-time-face-attribute-analysis.git
cd real-time-face-attribute-analysis
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Dependencies

This project uses the following dependencies:
```txt
Python==3.10.9
deepface==0.0.79
opencv-python==4.8.1.78
tensorflow==2.20.1
numpy==1.23.5
```

---

## Usage

Run the application:

```bash
python main.py
```

Press **Q** to quit.

---

## Optional Hybrid Approach

- Combine Haar Cascade for fast real-time detection with selective DeepFace analysis
- Analyze faces only every N frames and/or only if the face moves significantly
- Face movement checks to avoid redundant analysis
- Improves performance while maintaining good accuracy on CPU-limited systems

---

## Future Improvements

- Replace Haar Cascade with RetinaFace for higher accuracy
- Optional GPU acceleration for faster processing
- Dynamic face resizing for improved accuracy
- Add face tracking to maintain consistent labels for multiple faces
- Support video file input, not just live webcam
