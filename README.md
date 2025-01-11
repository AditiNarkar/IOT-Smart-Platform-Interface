# **Smart Platform Interface for Railway Passenger Movement and Safety Automation**

---

### **Overview**

This repository showcases the **Smart Platform Interface**, a research-backed IoT-based project designed to improve railway passenger movement and safety automation. Combining cutting-edge technologies such as NodeMCU, OpenCV, and YOLOv5, the system automates platform-to-platform passenger transfer while ensuring safety and efficiency.

This work includes both:

- A **research paper** outlining the methodology, implementation, and results.
- A **project implementation** demonstrating the practical application of the proposed solution.

---

### **Key Features**

#### **Research Highlights**:

- **Problem Addressed**: Provides solutions for congested and unsafe railway stations using automated mechanisms.
- **Methodology**: Introduced a novel approach using computer vision and IoT to enable real-time train detection and distance prediction.
- **Evaluation**: Extensive testing with custom datasets and performance metrics like precision, recall, F1 scores, and mean average precision (mAP).

#### **Project Implementation**:

- **Automated Train Detection**: Leverages YOLOv5 for object detection under varying environmental conditions.
- **Distance Prediction**: Employs a custom algorithm for accurate train-to-platform distance estimation.
- **Smart Platform Interface**:
  - Motorized platform controlled by NodeMCU.
  - Real-time alerts via LEDs and an LCD display.
  - Safety-first design with automated responses based on train proximity.

---

### **System Components**

#### **Hardware**:

- **NodeMCU (ESP8266)**: Central microcontroller for automation.
- **Servo Motors**: Controls platform movement.
- **LED Indicators**: Red and green lights for safety signals.
- **LCD Display (16x2)**: Displays real-time train information and alerts.
- **Camera Module**: Captures train movement for detection and distance prediction.
- **Power Supply**: Energizes all components.

#### **Software**:

- **YOLOv5**: Custom object detection model for train identification.
- **Python**: Handles train detection, distance prediction, and system control.
- **Blynk Cloud** (Optional): Remote monitoring and control of the interface.

---

### **How It Works**

1. **Train Detection**:
   - Captures real-time video using the camera module.
   - Identifies trains using YOLOv5 and calculates their distance.
2. **Safety Mechanism**:
   - If the train is within a critical distance:
     - Activates red LEDs.
     - Displays a warning message on the LCD.
     - Closes the platform interface using servo motors.
   - Once the train passes, green LEDs and an "All Clear" message are displayed, reopening the interface.
3. **Automation Control**:
   - NodeMCU orchestrates all actions, ensuring synchronized operation of LEDs, motors, and the LCD.

---

### **Motivation**

The project addresses critical safety and efficiency issues at railway stations, such as crowded footbridges and manual operations. By automating platform access, this solution enhances passenger convenience and reduces risks.

---

### **Research Paper**

The research paper, titled **"Smart Platform Interface for Railway Passenger Movement and Safety Automation,"** is available in this repository.  
**[Download Research Paper](/Smart%20Platform%20Interface%20Research%20Paper.pdf)**

It provides:

- **Background**: Challenges in railway passenger movement and the need for automation.
- **Proposed Solution**: Technical details of the Smart Platform Interface.
- **Results**: Evaluation of train detection accuracy and system performance.
- **Future Directions**: Suggestions for expanding functionality, including energy-efficient features and advanced sensors.

---

### **Future Work**

- **Energy Efficiency**: Integration of piezoelectric sensors for energy harvesting from footsteps.
- **Enhanced Safety**: UV sensors for train arrival alerts and solar-powered components for sustainability.
- **Scalability**: Adaptation for larger railway networks and varied train systems.

---

### **Authors**

- **Aditi Vikas Narkar** (UG Scholar, Terna Engineering College, Nerul, Navi Mumbai, India)  
  [adunarkar2004@gmail.com](mailto:adunarkar2004@gmail.com)
- **Muhammed Tufayl Dalvi** (UG Scholar, Terna Engineering College, Nerul, Navi Mumbai, India)  
  [tufayldalvi007@gmail.com](mailto:tufayldalvi007@gmail.com)
- **Dr. Sujata Kadu** (Professor, Terna Engineering College, Nerul, Navi Mumbai, India)  
  [sujatakadu@ternaengg.ac.in](mailto:sujatakadu@ternaengg.ac.in)

---

### **References**

Detailed references and citations are included in the research paper to help readers explore the underlying technologies and methodologies further.

---
