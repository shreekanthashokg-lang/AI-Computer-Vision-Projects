# 👁️ AI Computer Vision Projects

### My Computer Vision Journey with Python, OpenCV & YOLO

A practical **Computer Vision portfolio repository** documenting my journey from the fundamentals of image processing and computer vision to **real-time AI applications** using **Python, OpenCV, NumPy, and YOLOv8**.

This repository includes hands-on exercises, experiments, mini-projects, and real-time computer vision applications developed during my **5-Day Offline Computer Vision Hands-on Workshop by Innomatics Research Labs in July 2026**, along with additional projects developed to strengthen my practical AI/ML skills.

The goal of this repository is to demonstrate how computer vision concepts can be transformed into **working, real-world applications**.

---

## 📌ABOUT THIS REPOSITORY

Computer Vision is one of the most practical areas of Artificial Intelligence, enabling computers to understand and interpret images and videos.

This repository follows a progressive learning approach:

```text
Python & NumPy
      ↓
Image Processing
      ↓
OpenCV Fundamentals
      ↓
Video Processing
      ↓
Object Detection
      ↓
Object Tracking
      ↓
Real-Time Computer Vision
      ↓
YOLOv8
      ↓
AI-Based Applications
```

The projects range from basic OpenCV operations to real-time applications such as:

* 👤 Face Detection
* 📝 Face Attendance
* 🎯 Object Tracking
* 🚨 Motion Detection
* 🔍 Real-Time Object Detection
* 🤖 YOLOv8-based AI Detection

---

# 🎓 Completed COMPUTER VISION  Workshop

## 5-Day Offline Computer Vision Hands-on Workshop

**Organization:** Innomatics Research Labs
**Duration:** 5 Days
**Date:** July 2026
**Mode:** Offline Hands-on Workshop

The workshop provided practical exposure to computer vision concepts using Python and OpenCV.

The learning process focused on implementing concepts through code rather than only studying theoretical concepts.

### KEYS AREAS COVERED

* Python programming for Computer Vision
* NumPy operations
* Image reading and writing
* Image resizing and transformations
* Image color spaces
* Image filtering
* Edge detection
* Contour detection
* Image thresholding
* Webcam and video processing
* Object detection concepts
* Object tracking
* Real-time computer vision
* YOLO-based object detection

---

# 🛠️ TECHNOLOGIES & TOOLS 

| Technology          | Purpose                          |
| ------------------- | -------------------------------- |
| 🐍 Python           | Core programming language        |
| 👁️ OpenCV          | Image & video processing         |
| 🤖 YOLOv8           | Real-time object detection       |
| 🔢 NumPy            | Numerical and array operations   |
| 📊 Matplotlib       | Visualization and image analysis |
| 🧠 Ultralytics      | YOLO implementation              |
| 📄 CSV              | Attendance and event logging     |
| 💻 Jupyter Notebook | Experimentation and learning     |

---

# 📁 REPOSITORY STRUCTURE 

```text
AI-Computer-Vision-PROJECT/
│
├── README.md
│
├── Day-01/
│   ├── image_basics/
│   ├── image_reading/
│   └── image_processing/
│
├── Day-02/
│   ├── transformations/
│   ├── filtering/
│   └── edge_detection/
│
├── Day-03/
│   ├── contours/
│   ├── thresholding/
│   └── segmentation/
│
├── Day-04/
│   ├── video_processing/
│   ├── webcam/
│   └── object_tracking/
│
├── Day-05/
│   ├── object_detection/
│   ├── YOLO/
│   └── mini_projects/
│
├── mini-projects/
│   ├── face-attendance-system/
│   ├── color-object-tracker/
│   ├── motion-detection/
│   └── yolov8-object-detection/
│
├── data/
│
├── outputs/
│
├── requirements.txt
│
└── LICENSE
```

> The exact folder structure may evolve as additional computer vision projects are added.

---

# 🚀 MINI PROJECTS 

## 1️⃣LIVE FACE ATTENDANCE SYSTEM 

### 📌 Overview

The **Live Face Attendance System** is a real-time computer vision application designed to detect faces through a webcam and record attendance information.

The project demonstrates how computer vision can be used to automate a basic attendance workflow.

### 🔍 KEY FEATURES 

* Real-time webcam input
* Face detection
* Detection of multiple faces
* Attendance recording
* Timestamp generation
* CSV-based attendance logging
* Real-time visual feedback

### 🔄 Working Pipeline

```text
Webcam
   ↓
Capture Video Frame
   ↓
Face Detection
   ↓
Identify / Detect Face
   ↓
Check Attendance
   ↓
Record Name + Date + Time
   ↓
CSV Attendance File
```

### 💡 Practical Application

This type of system can be extended for:

* Classroom attendance
* Office attendance
* Training centers
* Workshops
* Laboratory environments

### 📈 Future Improvements

* Face recognition instead of only face detection
* Database integration
* Multiple-user recognition
* Anti-spoofing
* Web dashboard
* Cloud-based attendance records

---

# 2️⃣ 🎨 Real-Time Color Object Tracker

### 📌 Overview

The **Color Object Tracker** is a real-time computer vision project that detects and tracks an object based on its color.

The application processes webcam frames and identifies pixels belonging to a selected color range.

### 🔍 Key Concepts

* HSV color space
* Color masking
* Thresholding
* Contour detection
* Object center calculation
* Bounding boxes
* Real-time tracking

### 🔄 Working Pipeline

```text
Webcam Frame
      ↓
Convert BGR → HSV
      ↓
Define Color Range
      ↓
Create Color Mask
      ↓
Find Contours
      ↓
Identify Object
      ↓
Draw Bounding Box
      ↓
Track Object
```

### 💡 Practical Applications

The concept can be used as a foundation for:

* Industrial object tracking
* Robotic vision
* Gesture-based systems
* Automated sorting
* Color-based quality inspection

---

# 3️⃣ 🚨 Motion Detection & Alert System

### 📌 Overview

The **Motion Detection & Alert System** detects movement in a video stream by comparing consecutive frames.

When significant movement is detected, the system can generate an alert and log the event.

### 🔍 Key Features

* Real-time video monitoring
* Background/frame comparison
* Motion detection
* Contour-based movement identification
* Alert generation
* Event logging
* Timestamp support

### 🔄 Working Pipeline

```text
Video / Webcam
      ↓
Capture Frames
      ↓
Compare Consecutive Frames
      ↓
Calculate Difference
      ↓
Threshold
      ↓
Find Motion Regions
      ↓
Generate Alert
      ↓
Log Event
```

### 💡 Practical Applications

* Basic security monitoring
* Restricted-area monitoring
* Laboratory monitoring
* Smart surveillance
* Home monitoring
* Automated activity detection

### 📈 Future Improvements

* Email/SMS alerts
* Telegram notifications
* Person-specific detection
* Video recording
* Cloud storage
* YOLO integration

---

# 4️⃣ 🤖 YOLOv8 Real-Time Object Detection

### 📌 Overview

The **YOLOv8 Object Detection project** introduces deep-learning-based computer vision for detecting multiple objects in real time.

YOLO (**You Only Look Once**) is a popular object detection approach designed for fast object detection.

This project uses the **Ultralytics YOLOv8 framework** to detect common objects from images, videos, or webcam streams.

### 🔍 Key Features

* Real-time object detection
* Webcam support
* Image detection
* Video detection
* Bounding boxes
* Class labels
* Confidence scores
* Multiple-object detection

### 🔄 Working Pipeline

```text
Image / Video / Webcam
          ↓
        YOLOv8
          ↓
   Neural Network
          ↓
Object Detection
          ↓
Bounding Boxes
          ↓
Class Labels
          ↓
Confidence Scores
          ↓
Real-Time Output
```

### 🎯 Example Detection Classes

Depending on the selected pretrained model, the system can detect common objects such as:

* Person
* Car
* Bicycle
* Motorcycle
* Bus
* Truck
* Dog
* Cat
* Bottle
* Chair
* Laptop
* Cell phone

and many other pretrained classes.

### 💡 Practical Applications

YOLO-based systems can be extended to:

* Smart surveillance
* Traffic monitoring
* Retail analytics
* Industrial inspection
* Crowd monitoring
* Autonomous systems
* Safety monitoring
* Robotics

---

# 🧠 Computer Vision Concepts Practiced

Throughout this repository, I have worked with several important computer vision concepts.

### Image Processing

* Image loading
* Image saving
* Image resizing
* Image cropping
* Image rotation
* Image flipping
* Image enhancement

### Color Processing

* RGB/BGR
* Grayscale
* HSV
* Color masking

### Image Analysis

* Thresholding
* Edge detection
* Contours
* Morphological operations
* Segmentation

### Video Processing

* Webcam capture
* Video frames
* Frame-by-frame processing
* Real-time visualization

### Object Detection

* Bounding boxes
* Confidence scores
* Class prediction
* YOLO inference

### Object Tracking

* Color-based tracking
* Contour-based tracking
* Real-time object movement

---

# 📊 Learning Progress

This repository represents a progression from fundamental programming concepts to practical AI applications.

| Level           | Skills                                   |
| --------------- | ---------------------------------------- |
| 🟢 Beginner     | Python, NumPy, basic image operations    |
| 🟡 Intermediate | OpenCV, transformations, filtering       |
| 🟠 Advanced     | Contours, segmentation, video processing |
| 🔴 AI/ML        | YOLOv8, object detection                 |
| 🚀 Application  | Attendance, tracking, monitoring         |

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/shreekanthashokg-lang/AI-Computer-Vision-PROJECT.git
```

Move into the project:

```bash
cd AI-Computer-Vision-PROJECT
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 📦 Main Dependencies

Typical dependencies used throughout the projects include:

```text
Python
opencv-python
numpy
matplotlib
ultralytics
```

Additional dependencies may be added as individual projects evolve.

---

# ▶️ Running the Projects

Each mini-project contains its own implementation and instructions.

For example:

```bash
python face_attendance.py
```

or:

```bash
python color_tracker.py
```

or:

```bash
python motion_detection.py
```

For YOLO-based detection:

```bash
python yolo_detection.py
```

> Camera-based projects require a working webcam and appropriate camera permissions.

---

# 🎯 What I Learned

Through these projects, I developed practical experience in:

* Understanding how images are represented digitally
* Processing images using Python
* Working with OpenCV
* Handling real-time webcam streams
* Extracting useful information from images
* Detecting and tracking objects
* Understanding computer vision pipelines
* Working with pretrained YOLO models
* Building real-time AI applications
* Structuring computer vision projects for GitHub

More importantly, this journey helped me move from **learning computer vision concepts to implementing them as working applications**.

---

# 🚀 Future Roadmap

My next goal is to continue expanding this repository from traditional OpenCV projects toward more advanced AI-powered computer vision systems.

### 🔹 Phase 1 — Advanced OpenCV

* Advanced image processing
* Perspective transformation
* Image segmentation
* Background removal
* Advanced tracking

### 🔹 Phase 2 — YOLO

* Custom dataset creation
* Custom YOLO training
* Object detection
* Object tracking
* Model evaluation
* Model optimization

### 🔹 Phase 3 — MediaPipe

* Hand tracking
* Face landmarks
* Pose estimation
* Gesture recognition
* Human activity analysis

### 🔹 Phase 4 — AI Applications

* Smart attendance
* PPE detection
* Vehicle detection
* Number plate recognition
* People counting
* Crowd monitoring
* Safety monitoring

### 🔹 Phase 5 — Deployment

* Flask
* Streamlit
* REST APIs
* Web dashboards
* Docker
* Cloud deployment

---

# 🌟 Vision for This Repository

This repository is not intended to be just a collection of tutorial programs.

My objective is to continuously transform the projects into **practical, portfolio-level Computer Vision applications**.

```text
LEARN
  ↓
PRACTICE
  ↓
BUILD
  ↓
IMPROVE
  ↓
DEPLOY
  ↓
SOLVE REAL-WORLD PROBLEMS
```

I will continue adding projects, experiments, datasets, trained models, and deployment examples as I progress in my **AI/ML and Computer Vision journey**.

---

# 📚 Learning Journey

### July 2026

Completed a **5-Day Offline Computer Vision Hands-on Workshop by Innomatics Research Labs**, gaining practical exposure to Python, OpenCV, image processing, video processing, object detection, and real-time computer vision.

The workshop served as the foundation for this repository, which I am continuing to expand through independent projects and real-world applications.

---

# 🔮 Future Projects

Some planned projects include:

* 🤖 Custom YOLO Object Detector
* 👷 PPE / Safety Helmet Detection
* 🚗 Vehicle Detection & Counting
* 🔢 Automatic Number Plate Recognition
* 🧍 People Counting System
* ✋ Hand Gesture Recognition
* 🧑‍💻 Face Recognition Attendance
* 🏃 Human Activity Recognition
* 🏭 Industrial Object Detection
* 🚦 Traffic Monitoring System
* 🏥 Healthcare Computer Vision Applications

---

# 👨‍💻 About Me

**SHREEKANTH A GUTTEDAR**

MCA — AI/ML & Data Science

Interested in:

* Artificial Intelligence
* Machine Learning
* Data Science
* Computer Vision
* Deep Learning
* Python
* Real-Time AI Applications

I am continuously building practical projects to strengthen my technical skills and develop a strong AI/ML portfolio.

---

# 📫 Connect With Me

**LinkedIn:**
https://www.linkedin.com/in/shreekanthashokg/

**GitHub:**
https://github.com/shreekanthashokg-lang

---

# ⭐ Support

If you find this repository useful or interesting, consider giving it a ⭐ on GitHub.

More Computer Vision projects will be added as I continue learning, experimenting, and building.

---

### ❤️ Built with Python, OpenCV & AI

**Started during the Innomatics Research Labs Computer Vision Workshop — July 2026**

> **Learn → Build → Experiment → Deploy → Repeat.**
