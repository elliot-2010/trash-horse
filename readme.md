# 🐴 TRASH HORSE
### Smart Waste Sorting System

**Technology for Recycling and Automated Separation of Household Waste Horse**

TRASH HORSE is an embedded smart waste sorting system that combines **computer vision, machine learning, and electronics** to recognize waste objects and automate parts of the recycling process.

Developed using a Raspberry Pi 3, a camera, a TensorFlow Lite classification model, and servo motors, the system identifies waste categories and translates classification results into physical sorting actions.

---

## 🚀 Project Overview

The system captures images of waste objects through a camera connected to a Raspberry Pi. A machine learning model analyzes the images and predicts the corresponding waste category.

To improve prediction consistency, the application requires **four consecutive matching predictions** before executing a sorting action.

The Raspberry Pi then controls servo motors through its GPIO interface to direct supported waste categories toward their designated collection positions.

## ✨ Features

- **Computer Vision:** Image acquisition and preprocessing using OpenCV.
- **Machine Learning:** Local waste classification using TensorFlow Lite.
- **Embedded Processing:** Runs on a Raspberry Pi 3.
- **Servo Control:** Hardware control through GPIO Zero and pigpio.
- **Prediction Consistency:** Four consecutive matching predictions are required before a sorting action.
- **Local Inference:** Classification runs directly on the Raspberry Pi.

## 🧠 Classification Categories

The model recognizes five categories:

| Label | Description | Sorting Action |
|---|---|---|
| NTO | Non-trashable object | Not implemented |
| Metal | Metal waste | Servo 1 — GPIO18 |
| Plastic | Plastic waste | Servo 2 — GPIO19 |
| Paper | Paper waste | Servo 2 — GPIO19 |
| Glass | Glass waste | Not implemented |

**Note:** The model recognizes all five categories, but the current mechanical implementation only performs sorting movements for Metal, Plastic, and Paper.

## 🛠️ Hardware

| Component | Purpose |
|---|---|
| Raspberry Pi 3 | Main processing unit |
| Camera | Image acquisition |
| 2 × Servo motors | Mechanical sorting |
| Breadboard | Circuit prototyping |
| Jumper wires | Electrical connections |
| External power supply | Servo power |

The external servo power supply and Raspberry Pi must share a common ground.

## 💻 Software and Technologies

- **Python** — Main programming language
- **OpenCV** — Camera access and image processing
- **NumPy** — Numerical operations and array manipulation
- **TensorFlow Lite** — Machine learning inference
- **GPIO Zero** — GPIO and servo control
- **pigpio** — GPIO control backend
- **Raspberry Pi OS** — Embedded operating system

## ⚙️ System Architecture

```text
       Camera
          |
          v
   OpenCV Processing
          |
          v
  Image Preprocessing
          |
          v
 TensorFlow Lite Model
          |
          v
 Classification Result
          |
          v
 Four-Prediction Check
          |
          v
   Sorting Decision
          |
          v
    GPIO Control
          |
          v
     Servo Motors
          |
          v
   Sorting Mechanism
```

## 🔧 Installation and Setup

### Requirements

- Raspberry Pi 3
- Raspberry Pi OS
- Python 3
- Connected camera
- Servo motors and external power supply

### Install Dependencies

Install the required Python libraries in an appropriate Python environment:

```bash
pip install numpy opencv-python gpiozero
```

TensorFlow Lite and pigpio must also be installed and configured for the Raspberry Pi OS environment.

### Model Setup

Place the trained TensorFlow Lite model in the project directory:

```text
model.tflite
```

The application loads this model for local image classification.

### Run the Application

After configuring the hardware, dependencies, and camera:

```bash
python3 main.py
```

Make sure the required GPIO backend is available and configured before running the application.

## 👨‍💻 Team

**Mohammadreza Kermani**
- Raspberry Pi and Linux configuration
- Python application integration
- GPIO and servo control
- Electronics and hardware integration

**Ilia Bakhshayesh**
- Machine learning model development
- Model training
- Image processing
- Classification implementation

Both contributors worked on the overall system integration.

## 🔮 Future Improvements

- Implement mechanical sorting for Glass and NTO.
- Improve classification reliability with additional training data.
- Optimize inference performance.
- Improve the mechanical sorting mechanism.
- Add a graphical user interface.
- Introduce system monitoring and sorting statistics.

## 📄 Technical Documentation

For a detailed explanation of the project, including its architecture, implementation, hardware, testing, and development process, see:

**[TRASH HORSE — Technical Project Report](docs/TRASH_HORSE_Technical_Project_Report.md)**

## 🤖 AI Declaration

AI tools were used as supplementary learning and educational assistance during development. The project was implemented through the authors' own programming, experimentation, hardware integration, and technical work. It is not a fully AI-generated project.

---

**TRASH HORSE**  
*Turning waste recognition into automated action.*
