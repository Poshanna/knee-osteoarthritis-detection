# 🦴 Knee Osteoarthritis Detection using X-ray Images

## 📌 Project Overview

Knee Osteoarthritis (OA) is one of the most common degenerative joint diseases affecting millions of people worldwide. Early diagnosis and severity assessment help clinicians recommend appropriate treatment and improve patient outcomes.

This project presents a Deep Learning-based web application that analyzes knee X-ray images and predicts the severity of Osteoarthritis using the Kellgren-Lawrence (KL) grading system. The application also provides Grad-CAM explainability, confidence scores, and clinical recommendations through an interactive Streamlit interface.

The project is deployed on Streamlit Cloud and integrated with GitHub for version control and continuous deployment.

---

## 🎯 Objectives

* Detect Knee Osteoarthritis from X-ray images.
* Classify Osteoarthritis severity using KL Grades.
* Provide visual explanations using Grad-CAM heatmaps.
* Display model performance metrics.
* Create an interactive and user-friendly web application.
* Demonstrate Explainable AI (XAI) in healthcare applications.

---

## 🚀 Live Demo

🌐 **Streamlit Application**

https://knee-osteoarthritis-detection-in7jxo4o5ioykj8w4oqupd.streamlit.app/

---

## 🔗 GitHub Repository

https://github.com/Poshanna/knee-osteoarthritis-detection

---

## ✨ Features

### ✅ X-ray Image Upload

Upload knee X-ray images in JPG, JPEG, or PNG format.

### ✅ Automated OA Grading

Predicts Osteoarthritis severity using:

* Grade 0 – Normal
* Grade 1 – Doubtful
* Grade 2 – Minimal
* Grade 3 – Moderate
* Grade 4 – Severe

### ✅ Confidence Score

Displays confidence percentage for each prediction.

### ✅ Clinical Recommendations

Provides diagnosis-specific recommendations.

### ✅ Grad-CAM Explainability

Visual heatmaps highlight the regions influencing model decisions.

### ✅ Performance Dashboard

Displays:

* Accuracy Graph
* Loss Graph
* Confusion Matrix
* Sample Predictions

### ✅ Interactive Web Interface

Built using Streamlit for easy accessibility.

---

## 🧠 Technology Stack

| Technology      | Purpose             |
| --------------- | ------------------- |
| Python          | Core Programming    |
| Streamlit       | Web Application     |
| PyTorch         | Deep Learning       |
| OpenCV          | Image Processing    |
| NumPy           | Numerical Computing |
| Pandas          | Data Analysis       |
| Matplotlib      | Data Visualization  |
| Pillow (PIL)    | Image Handling      |
| GitHub          | Version Control     |
| Streamlit Cloud | Deployment          |

---

## 📂 Project Structure

```text
knee-osteoarthritis-detection/
│
├── app.py
├── requirements.txt
├── packages.txt
├── README.md
│
├── utils/
│   ├── __init__.py
│   └── predictor.py
│
├── grade0.png
├── grade1.png
├── grade2.png
├── grade3.png
├── grade4.png
│
├── normal.jpg
├── osteoarthritis.jpg
│
├── accuracy_graph.png
├── loss_graph.png
├── confusion_matrix.png
├── gradcam_examples.png
├── sample_predictions.png
│
├── generate_assets.py
├── generate_presentation.py
└── Presentation_Slides.txt
```

---

## 📊 Model Performance

### Performance Metrics

| Metric    | Score  |
| --------- | ------ |
| Accuracy  | 92.95% |
| Precision | 91.80% |
| Recall    | 92.10% |
| F1-Score  | 91.95% |

### Performance Visualizations

* Training Accuracy Curve
* Validation Accuracy Curve
* Training Loss Curve
* Validation Loss Curve
* Confusion Matrix
* Sample Predictions
* Grad-CAM Heatmaps

---

## 🔥 Explainable AI using Grad-CAM

Grad-CAM (Gradient-weighted Class Activation Mapping) is used to visualize the important regions of the knee joint that contribute to the prediction.

### Benefits

* Improves model transparency
* Supports clinical interpretation
* Highlights joint-space narrowing
* Assists healthcare professionals in decision-making

---

## 🩺 Clinical Severity Classification

| Grade   | Description  |
| ------- | ------------ |
| Grade 0 | Normal Joint |
| Grade 1 | Doubtful OA  |
| Grade 2 | Minimal OA   |
| Grade 3 | Moderate OA  |
| Grade 4 | Severe OA    |

---

## 💻 Installation & Local Setup

### Clone Repository

```bash
git clone https://github.com/Poshanna/knee-osteoarthritis-detection.git
cd knee-osteoarthritis-detection
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit Application

```bash
streamlit run app.py
```

---

## 📷 Application Workflow

1. Upload Knee X-ray Image.
2. Run Diagnostic Analysis.
3. Predict KL Grade.
4. Display Confidence Score.
5. Generate Grad-CAM Heatmap.
6. Provide Clinical Recommendation.
7. Visualize Model Performance.

---

## 🎓 Academic Relevance

This project demonstrates practical applications of:

* Artificial Intelligence
* Machine Learning
* Deep Learning
* Medical Image Analysis
* Computer Vision
* Explainable AI (XAI)
* Healthcare Analytics
* Web-based AI Deployment

---

## 🏆 Key Highlights

* Interactive Streamlit Application
* Deep Learning-based OA Classification
* Grad-CAM Explainability
* Clinical Decision Support
* GitHub Version Control
* Cloud Deployment using Streamlit

---

## 👨‍💻 Developer

**Durki Poshanna**

B.E. Artificial Intelligence & Machine Learning

Chaitanya Bharathi Institute of Technology (CBIT)

GitHub Profile:
https://github.com/Poshanna

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

Thank you for visiting this repository!
