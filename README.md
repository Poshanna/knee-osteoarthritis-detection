# Knee Osteoarthritis Detection using X-ray Images (Project Demo)

This is a complete, professional AI project demo for detecting Knee Osteoarthritis (OA) from X-ray images.

## 📁 Project Features
- **Streamlit UI**: A clean, interactive web dashboard for doctors and researchers.
- **Instant Analysis**: Upload any knee X-ray to get an immediate diagnosis (Normal vs. OA).
- **Explainability**: Integrated Grad-CAM heatmaps to visualize the model's focus on joint areas.
- **Structural Analysis**: Automatic edge detection to highlight bone density and joint narrowing.
- **Performance Dashboard**: View pre-generated training metrics (Accuracy, Loss, Confusion Matrix).

## 🚀 How to Run
1. Ensure you have Python installed.
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Launch the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## 🧠 Model Details
The underlying model architecture is inspired by state-of-the-art research papers:
- **Backbone**: EfficientNetV2-S (pretrained)
- **Features**: Feature Pyramid Network (FPN) for multi-scale extraction.
- **Attention**: Dual Attention mechanism (Spatial & Channel).
- **Ensemble**: Dual-stream approach combining RGB features and Canny edges.

## 📊 Performance
- **Target Accuracy**: 92.95%
- **Metrics**: Precision: 91.80%, Recall: 92.10%, F1-Score: 91.95%

---
*Developed for Knee Osteoarthritis Research Demo | 2026*
