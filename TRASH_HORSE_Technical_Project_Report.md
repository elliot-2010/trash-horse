# TRASH HORSE --- Technical Project Report

# SMART WASTE SORTING SYSTEM

# TECHNICAL PROJECT REPORT

Technology for Recycling and Automated Separation\
of Household Waste Horse

Project Authors\
Mohammadreza Kermani \| Ilia Bakhshayesh

Educational Institution\
Aboozar Vocation School

Field of Study\
Computer Science / Network and Software

Project Supervisor\
Mr. Hashemi

Date\
Nov 14 2026

# Abstract

Waste management and recycling are important challenges in modern
society. One difficulty in the recycling process is separating different
types of waste into appropriate categories. Manual waste sorting
requires human involvement and can be time-consuming.

This project, named TRASH HORSE, aims to develop a smart waste sorting
system that combines computer vision, machine learning, and embedded
hardware to automate parts of the waste separation process.

The system uses a Raspberry Pi 3 as its main processing unit. A camera
captures images of waste objects, and a machine learning model processes
these images to identify their categories. The classification model,
developed using Google's machine learning technology and trained by Ilia
Bakhshayesh, is deployed in TensorFlow Lite format to enable local
inference on the Raspberry Pi.

After classification, Python software processes the predictions and
controls two servo control channels through the Raspberry Pi GPIO
interface. The servo mechanisms direct recognized waste categories
toward their corresponding collection positions.

The software is developed using Python and several libraries, including
OpenCV, NumPy, TensorFlow Lite, and GPIO Zero.

This project demonstrates the integration of computer vision, machine
learning, embedded Linux, electronics, and mechanical control in a
practical automated system.

Keywords: Raspberry Pi, Python, Computer Vision, TensorFlow Lite,
OpenCV, GPIO, Servo Motor, Waste Classification, Automation.

# Table of Contents

## Contents

The section headings below form the table of contents in Markdown
viewers that support heading navigation.

# 1. Introduction

## 1.1 Background

Waste separation is an important part of effective recycling systems.
Different materials, such as paper, plastic, metal, and glass, require
different recycling processes.

In conventional waste collection systems, separation is frequently
performed manually or through specialized industrial equipment.

Recent developments in computer vision and machine learning have created
opportunities to automate waste recognition and sorting using relatively
affordable hardware.

Embedded computers, such as the Raspberry Pi, make it possible to
implement these technologies in compact systems without requiring a full
desktop computer.

## 1.2 Project Description

TRASH HORSE is an automated waste recognition and sorting project
designed to identify waste categories using a camera and a machine
learning model.

The project combines two main technological areas:

-   Artificial Intelligence and Computer Vision: recognizing waste
    objects from camera images.
-   Embedded Systems and Electronics: controlling mechanical components
    according to classification results. The Raspberry Pi acts as the
    central processing unit, coordinating communication between the
    camera, classification software, and servo motors.

The system is designed to reduce the amount of manual work required
during waste separation.

## 1.3 Project Motivation

The main motivation behind this project was to explore how software and
hardware technologies can work together to solve a practical
environmental problem.

Rather than developing a purely software-based application, the team
aimed to create a physical prototype capable of interacting with its
environment.

The project also provided an opportunity to gain practical experience in
Linux, Python programming, machine learning, electronics, and hardware
integration.

# 2. Project Objectives

The primary objective is to develop a prototype capable of recognizing
waste objects and directing them toward appropriate collection
positions.

The specific objectives include:

1.  Developing a machine learning-based waste classification system.
2.  Deploying the trained model on a Raspberry Pi 3.
3.  Capturing images using a connected camera.
4.  Processing images using OpenCV and NumPy.
5.  Executing the classification model locally using TensorFlow Lite.
6.  Controlling servo motors through the Raspberry Pi GPIO interface.
7.  Integrating software and hardware into a unified system.
8.  Testing the reliability of classification and mechanical control.
    \# 3. Project Overview and Scope

## 3.1 General Operation

The system follows a sequence of operations:

1.  A waste object is presented to the camera.
2.  The camera captures an image.
3.  OpenCV processes the image and prepares it for classification.
4.  The TensorFlow Lite interpreter executes the machine learning model.
5.  The model produces a classification result.
6.  The program collects multiple consecutive predictions.
7.  If four consecutive predictions agree, the software determines the
    appropriate sorting action.
8.  The corresponding servo motor moves to its assigned position.
9.  After the movement, the servo returns to its neutral position. \##
    3.2 Classification Categories

The software currently defines five classification labels. NTO means
"Non-trashable object":

  Category   Description
  ---------- ----------------------
  NTO        Non-trashable object
  Metal      Metal waste
  Plastic    Plastic waste
  Paper      Paper waste
  Glass      Glass waste

The classification model can identify these five categories. However,
the current mechanical implementation only performs servo movements for
Metal, Plastic, and Paper.

Glass and NTO currently produce classification messages without
activating a sorting mechanism. This distinction is important when
evaluating the implemented functionality.

# 4. Hardware Requirements

The project combines an embedded computer, electronic components, and
mechanical actuators.

## 4.1 Raspberry Pi 3

The Raspberry Pi 3 is the main processing unit of the system.

It is responsible for:

-   Running the operating system.
-   Executing the Python application.
-   Processing camera images.
-   Running the TensorFlow Lite model.
-   Managing GPIO communication.
-   Controlling the servo motors. The Raspberry Pi was selected because
    of its relatively small size, low power consumption, Linux
    compatibility, and GPIO capabilities.

\[ Insert a Raspberry Pi 3 reference image \]

*Figure 1. Raspberry Pi 3 single-board computer.*

## 4.2 SG90 Servo Motors

The project uses two servo control channels to operate the mechanical
sorting mechanism. The servo motors receive control signals from the
Raspberry Pi and move to specified angular positions.

The software uses the AngularServo class from GPIO Zero to control their
positions.

  Servo     GPIO Pin   Physical Pin
  --------- ---------- --------------
  Servo 1   GPIO18     Pin 12
  Servo 2   GPIO19     Pin 35

The servo positions used by the program include 0°, 90°, and 180°. The
90° position is used as the neutral position in the control routine.

\[ Insert an SG90 servo reference image \]

*Figure 2. SG90 micro servo motor.*

## 4.3 Breadboard and Electrical Connections

A breadboard and jumper wires are used to establish the required
electrical connections between the Raspberry Pi and the servo control
circuits.

The servo motors require an appropriate power supply. An external power
source is used to provide servo power.

A common ground connection between the external power supply and the
Raspberry Pi is necessary to establish a shared electrical reference for
the control signals.

\[ Insert a breadboard and wiring reference image \]

*Figure 3. Illustrative breadboard and electronic connections.*

## 4.4 Camera

A camera is connected to the Raspberry Pi to capture images of waste
objects. The camera provides the input data required by the machine
learning model.

The software accesses the camera using OpenCV's VideoCapture interface.

\[ Insert a camera reference image \]

*Figure 4. Camera module used for image acquisition.*

## 4.5 Hardware Summary

  Component               Function
  ----------------------- ------------------------
  Raspberry Pi 3          Main processing unit
  Camera                  Image acquisition
  SG90 servo motors       Mechanical movement
  Breadboard              Circuit prototyping
  Jumper wires            Electrical connections
  External power supply   Servo power

# 5. Software and Technologies

The TRASH HORSE system uses several software technologies to combine
computer vision, machine learning, and embedded hardware control.

## 5.1 Python

Python is the primary programming language used in the project. It
coordinates the different software components, including camera
communication, image preprocessing, model inference, and servo motor
control.

Python was selected because of its extensive ecosystem of libraries for
artificial intelligence, computer vision, and hardware programming.

## 5.2 OpenCV

OpenCV (Open Source Computer Vision Library) is used for camera
communication and image processing.

Its main responsibilities include:

-   Accessing the connected camera.
-   Capturing image frames.
-   Converting images from BGR to RGB color format.
-   Resizing images according to the machine learning model's input
    dimensions. OpenCV provides the image data required by the
    classification model.

## 5.3 TensorFlow Lite

TensorFlow Lite is the machine learning inference framework used by the
project.

The classification model, named TRASH HORSE, is provided in the .tflite
format. The model was trained by Ilia Bakhshayesh using Google's machine
learning technology.

TensorFlow Lite allows the model to execute directly on the Raspberry Pi
without requiring an external cloud-based inference service.

The program uses the TensorFlow Lite Interpreter to:

1.  Load the model file.
2.  Allocate the required tensors.
3.  Retrieve input and output information.
4.  Receive processed image data.
5.  Execute model inference.
6.  Retrieve classification predictions. This approach enables local
    image classification on the embedded device.

## 5.4 NumPy

NumPy is used for numerical calculations and image data manipulation.

Its functions support:

-   Expanding image dimensions.
-   Converting image data into numerical arrays.
-   Applying normalization and quantization transformations.
-   Finding the highest-scoring classification result. NumPy provides
    the numerical operations needed to prepare images and interpret
    model outputs.

## 5.5 GPIO Zero

GPIO Zero is the Python library used to control the Raspberry Pi GPIO
interface.

The project uses its AngularServo class to control the angular positions
of the servo motors. The software creates two independent servo objects
connected to GPIO18 and GPIO19.

The motors are controlled by assigning angular values to their
respective objects.

## 5.6 pigpio

The project uses PiGPIOFactory as the GPIO Zero pin factory. This
backend provides the servo control interface used by the application.

It is configured when creating the servo objects, allowing the
application to use the pigpio-based GPIO control system. The required
pigpio service and compatibility must be maintained in the operating
system environment.

## 5.7 Software Summary

  Technology        Application
  ----------------- -----------------------------------------------
  Python            Main programming language
  OpenCV            Camera communication and image processing
  TensorFlow Lite   Machine learning inference
  NumPy             Numerical calculations and array manipulation
  GPIO Zero         Servo motor control
  pigpio            GPIO control backend
  Raspberry Pi OS   Embedded operating system

# 6. System Architecture

## 6.1 General Architecture

The system consists of three major functional layers:

1.  Image Acquisition Layer

The camera captures images of waste objects. OpenCV retrieves the frames
and prepares the image data.

2.  Classification Layer

The TensorFlow Lite interpreter processes the prepared image and
generates a classification result.

3.  Hardware Control Layer

The Python application evaluates the classification results and
determines whether a servo motor should move.

## 6.2 System Workflow

The complete processing pipeline can be represented as follows:

Camera Input

↓

OpenCV Image Processing

↓

Image Resizing and Normalization

↓

TensorFlow Lite Inference

↓

Classification Result

↓

Four-Prediction Consistency Check

↓

Sorting Decision

↓

GPIO Servo Control

↓

Mechanical Sorting Action

## 6.3 Image Processing

The input image is initially captured in BGR format by OpenCV. The
program converts it into RGB format because the model expects RGB image
data.

The image is then resized according to the input dimensions obtained
from the TensorFlow Lite model. The image is expanded into a batch of
one image and converted into a numerical representation.

Normalization and quantization are applied according to the model's
input parameters. This process ensures that the image is prepared in the
format expected by the model.

## 6.4 Classification Process

The TensorFlow Lite interpreter executes the classification model. The
model produces numerical output values representing its predictions.

The program identifies the index of the highest-scoring output using
NumPy's argmax function. This index is then mapped to the corresponding
category name through a predefined classification list.

## 6.5 Prediction Consistency Mechanism

Instead of immediately responding to every individual prediction, the
program collects four consecutive classification results. The system
checks whether all four results are identical.

If they agree, the corresponding sorting action is selected. If they
disagree, the current group of predictions is discarded and a new group
begins.

This mechanism is intended to reduce reactions to individual
inconsistent predictions.

# 7. Implementation

## 7.1 Software Development Environment

The main application is developed in Python and runs on the Raspberry
Pi. The program integrates image acquisition, machine learning
inference, and hardware control in a single application.

The main software dependencies include:

-   OpenCV
-   NumPy
-   TensorFlow
-   GPIO Zero
-   pigpio \## 7.2 Servo Initialization

At the beginning of the main function, the program initializes the
pigpio pin factory. Two AngularServo objects are created: the first
servo is connected to GPIO18, and the second servo is connected to
GPIO19.

Both servos are configured with a minimum angle of 0° and a maximum
angle of 180°.

The pulse-width parameters are configured as follows:

-   Minimum pulse width: 0.0005 seconds.
-   Maximum pulse width: 0.0025 seconds. After initialization, the
    program moves both servos to their neutral positions.

## 7.3 Model Initialization

The TensorFlow Lite model is loaded using the Interpreter class. The
program allocates the model's tensors and retrieves its input and output
information.

The input dimensions and quantization parameters are obtained
dynamically from the model. This allows the application to prepare image
data according to the model's configuration rather than relying entirely
on hardcoded image dimensions.

## 7.4 Camera Initialization

OpenCV's VideoCapture function is used to access the camera. The camera
index is supplied as a function argument.

If the camera cannot be opened, the program displays an error message
and closes the initialized hardware resources.

## 7.5 Image Processing and Inference

The application continuously reads camera frames. Classification
inference is performed at intervals of approximately 0.5 seconds.

Before inference, the frame is:

1.  Converted from BGR to RGB.
2.  Resized to the model's input dimensions.
3.  Expanded into a batch.
4.  Converted and normalized.
5.  Quantized according to the model's input parameters. The prepared
    image is passed to the TensorFlow Lite interpreter. After inference,
    the output tensor is retrieved and converted using the output
    quantization parameters. The highest-scoring category is selected as
    the prediction.

## 7.6 Servo Control Logic

The servo control function receives a servo object and a target angle.

It performs the following operations:

1.  Moves the servo to the requested angle.
2.  Waits for two seconds.
3.  Returns the servo to 90°.
4.  Waits for another two seconds. The sorting logic currently uses the
    following mapping:

  Classification   Servo          Target angle
  ---------------- -------------- -----------------
  Metal            GPIO18 servo   0°
  Plastic          GPIO19 servo   0°
  Paper            GPIO19 servo   180°
  Glass            No movement    Not implemented
  NTO              No movement    Not implemented

This mapping represents the current software implementation.

## 7.7 Resource Management

The application includes a try/finally structure to manage resources.

When the program exits or encounters an error during the main processing
loop, the cleanup section releases:

-   The camera.
-   OpenCV windows.
-   Both servo objects.
-   The pigpio pin factory. This helps prevent hardware resources from
    remaining unnecessarily occupied after the application terminates.

# 8. Testing and Evaluation

Testing is an important part of evaluating the performance and
reliability of an embedded system. The project requires testing at both
the individual component level and the complete system level.

## 8.1 Hardware Testing

Hardware testing focuses on verifying the electrical connections and
mechanical components.

  Test                   Expected Result            Actual Result
  ---------------------- -------------------------- -------------------
  Raspberry Pi startup   Successful startup         \[Record result\]
  GPIO18 output          Correct servo control      \[Record result\]
  GPIO19 output          Correct servo control      \[Record result\]
  External servo power   Stable motor operation     \[Record result\]
  Common ground          Reliable control signals   \[Record result\]
  Camera connection      Successful image capture   \[Record result\]

## 8.2 Software Testing

Software testing focuses on the application's ability to execute the
classification and control procedures.

  -----------------------------------------------------------------------
  Test                    Expected Result         Actual Result
  ----------------------- ----------------------- -----------------------
  Model loading           Successful model        \[Record result\]
                          initialization          

  Camera access           Continuous frame        \[Record result\]
                          acquisition             

  Image preprocessing     Correct input           \[Record result\]
                          preparation             

  Model inference         Classification output   \[Record result\]

  Prediction consistency  Four matching           \[Record result\]
                          predictions detected    

  Program termination     Hardware resources      \[Record result\]
                          released                
  -----------------------------------------------------------------------

## 8.3 Classification Testing

Each classification category should be tested using multiple
representative objects. The results should be recorded to evaluate the
model's performance.

  Category   Number of Tests   Correct Predictions   Accuracy
  ---------- ----------------- --------------------- ----------
  Metal      \[ \]             \[ \]                 \[ \]
  Plastic    \[ \]             \[ \]                 \[ \]
  Paper      \[ \]             \[ \]                 \[ \]
  Glass      \[ \]             \[ \]                 \[ \]
  NTO        \[ \]             \[ \]                 \[ \]

Accuracy can be calculated using:

Accuracy = (Correct Predictions / Total Tests) × 100

Actual test results should be entered after performing the experiments.

## 8.4 Complete System Testing

The final testing stage evaluates the interaction between the camera,
machine learning model, Python application, and servo motors. The
objective is to verify that a recognized category results in the
appropriate mechanical action.

\[ Insert photographs of the actual testing process \]

# 9. Challenges and Solutions

During the development process, several technical challenges were
encountered.

## 9.1 Servo Motor Instability

One of the challenges occurred during servo motor operation. The servos
sometimes moved irregularly or failed to respond consistently.

After examining the electrical connections, it was discovered that the
external power supply's ground was not connected to the Raspberry Pi's
ground.

The problem was addressed by connecting the grounds of both power
systems. This established a common electrical reference for the servo
control signals.

## 9.2 Image Processing Compatibility

Machine learning models require input images with specific dimensions,
color formats, and numerical representations.

To address this, the software retrieves the required input dimensions
and quantization parameters directly from the TensorFlow Lite
interpreter. OpenCV and NumPy are then used to prepare the image data.

## 9.3 Prediction Stability

Individual classification results may occasionally differ because of
changes in object position, lighting, or camera conditions.

To reduce the effect of individual inconsistent predictions, the program
collects four consecutive predictions and checks whether they agree
before performing a sorting action.

## 9.4 Hardware and Software Integration

Another important challenge was coordinating the image classification
process with the physical servo mechanisms.

The software needed to translate classification results into appropriate
mechanical actions. This was addressed by implementing a control
function that receives a servo object and a target angle. The
classification logic then selects the appropriate servo and position.

# 10. Team Contributions

The project was developed collaboratively by Mohammadreza Kermani and
Ilia Bakhshayesh. Responsibilities were divided according to the
different technical areas of the system.

## 10.1 Mohammadreza Kermani

Primary responsibilities:

-   Raspberry Pi configuration and setup.
-   Linux operating system and environment management.
-   Python application development and integration.
-   GPIO configuration.
-   Servo motor control and testing.
-   Electronic connections and hardware integration.
-   Communication between software and physical components. \## 10.2
    Ilia Bakhshayesh

Primary responsibilities:

-   Machine learning model development.
-   Training the TRASH HORSE classification model.
-   Image processing implementation.
-   Development and integration of classification functionality. \##
    10.3 Collaborative Work

Both team members contributed to the overall development and integration
of the project. The software and hardware components were brought
together to create a unified waste sorting prototype.

# 11. Limitations and Future Improvements

Although the current implementation demonstrates the integration of
machine learning and embedded hardware, several improvements can be
considered.

## 11.1 Additional Sorting Categories

The current classification model recognizes five labels, but the
mechanical system does not yet provide a dedicated sorting action for
every category. Future development could include mechanical sorting
positions for Glass and additional waste categories.

## 11.2 Classification Reliability

The classification system could be improved through additional training
data, better image diversity, and more extensive testing under different
lighting conditions.

## 11.3 Mechanical Improvements

The mechanical sorting mechanism could be redesigned to improve
reliability, positioning accuracy, and overall durability.

## 11.4 Performance Optimization

The software could be optimized to reduce unnecessary processing and
improve inference performance on the Raspberry Pi.

## 11.5 User Interface

A future version could include a graphical interface displaying:

-   Camera output.
-   Current classification.
-   Servo status.
-   Number of processed objects.
-   System operating status. \## 11.6 System Monitoring

Additional monitoring features could be implemented to detect camera
failures, servo errors, and unexpected system behavior.

# 12. Conclusion

TRASH HORSE demonstrates how machine learning, computer vision, embedded
Linux, and electronics can be combined to develop a practical automated
waste sorting prototype.

The project uses a Raspberry Pi 3 as its central processing unit, OpenCV
for camera communication and image processing, TensorFlow Lite for
machine learning inference, and GPIO Zero with pigpio for servo control.

One of the main achievements of the project is the integration of a
trained classification model with physical hardware. Rather than simply
identifying objects on a computer screen, the system uses classification
results to control mechanical components.

The development process also provided practical experience in Linux
system configuration, Python programming, electronic circuit
connections, image processing, machine learning deployment, and
hardware-software integration.

Although the current implementation has limitations, particularly
regarding the mechanical handling of all classification categories, it
establishes a foundation for further development.

TRASH HORSE represents an interdisciplinary engineering project that
demonstrates the potential of accessible computing technologies in
addressing practical environmental challenges.

# 13. References

The following official documentation and resources provide technical
information about the technologies used in this project.

1.  Python Software Foundation. Python Documentation.
    https://docs.python.org/3/
2.  OpenCV. OpenCV Documentation. https://docs.opencv.org/
3.  Google. TensorFlow Lite Documentation.
    https://www.tensorflow.org/lite
4.  NumPy Developers. NumPy Documentation. https://numpy.org/doc/
5.  Raspberry Pi Foundation. Raspberry Pi Documentation.
    https://www.raspberrypi.com/documentation/
6.  GPIO Zero. GPIO Zero Documentation. https://gpiozero.readthedocs.io/
7.  pigpio. pigpio Library Documentation. http://abyz.me.uk/rpi/pigpio/
8.  TowerPro. SG90 Micro Servo Motor Specifications. \[Insert the exact
    manufacturer datasheet used.\] \# 14. Appendix

## Appendix A -- Software Implementation

The main application is written in Python and integrates the following
components:

-   Camera acquisition through OpenCV.
-   Image preprocessing using OpenCV and NumPy.
-   Machine learning inference through TensorFlow Lite.
-   Prediction evaluation.
-   Servo motor control using GPIO Zero and pigpio. The source code is
    maintained by the project authors, Ilia Bakhshayesh and Mohammadreza
    Kermani.

## Appendix B -- Project Documentation

The following materials should accompany the report:

-   Photograph of the Raspberry Pi 3.
-   Photograph of the servo motors.
-   Illustrative electrical connection diagram.
-   Screenshot of the software running on the Raspberry Pi.
-   Actual photographs of the completed prototype.
-   Demonstration video of the sorting process. \## Appendix C --
    Project Ownership and AI Declaration

### Project Ownership

The source code and project implementation are the property of Ilia
Bakhshayesh and Mohammadreza Kermani.

### Artificial Intelligence Declaration

Artificial intelligence tools were used as supplementary learning and
educational assistance during the development process. The project was
developed through the authors' own programming, experimentation,
hardware integration, and technical work. It was not generated as a
fully automated AI-written project.

### Machine Learning Model

The TRASH HORSE classification model was developed using Google's
machine learning technology and trained by Ilia Bakhshayesh.

### Project Name

TRASH HORSE stands for:

Technology for Recycling and Automated Separation\
of Household Waste Horse
