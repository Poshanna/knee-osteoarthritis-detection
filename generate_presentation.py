"""
Knee Osteoarthritis Detection - PowerPoint Presentation Generator
Run this script on your local machine to generate the 15-slide presentation.

IMPORTANT: Install python-pptx first by running:
    pip install python-pptx

Then run this script:
    python generate_presentation.py
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RgbColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
import os

def add_title_slide(prs, title, subtitle):
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)
    
    # Background shape
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.33), Inches(7.5))
    shape.fill.solid()
    shape.fill.fore_color.rgb = RgbColor(26, 35, 126)
    shape.line.fill.background()
    
    # Title
    txBox = slide.shapes.add_textbox(Inches(1), Inches(2.5), Inches(11), Inches(1.5))
    tf = txBox.text_frame
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(48)
    p.font.bold = True
    p.font.color.rgb = RgbColor(255, 255, 255)
    p.alignment = PP_ALIGN.CENTER
    
    # Subtitle
    txBox2 = slide.shapes.add_textbox(Inches(1), Inches(4.5), Inches(11), Inches(1))
    tf2 = txBox2.text_frame
    p2 = tf2.paragraphs[0]
    p2.text = subtitle
    p2.font.size = Pt(24)
    p2.font.color.rgb = RgbColor(197, 202, 233)
    p2.alignment = PP_ALIGN.CENTER
    
    return slide

def add_content_slide(prs, title, bullets, image_path=None):
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)
    
    # Header bar
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.33), Inches(1.2))
    shape.fill.solid()
    shape.fill.fore_color.rgb = RgbColor(30, 136, 229)
    shape.line.fill.background()
    
    # Title
    txBox = slide.shapes.add_textbox(Inches(0.5), Inches(0.25), Inches(12), Inches(0.8))
    tf = txBox.text_frame
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = RgbColor(255, 255, 255)
    
    # Content
    txBox2 = slide.shapes.add_textbox(Inches(0.7), Inches(1.6), Inches(6), Inches(5.5))
    tf2 = txBox2.text_frame
    tf2.word_wrap = True
    
    for i, bullet in enumerate(bullets):
        if i == 0:
            p = tf2.paragraphs[0]
        else:
            p = tf2.add_paragraph()
        p.text = f"• {bullet}"
        p.font.size = Pt(18)
        p.font.color.rgb = RgbColor(50, 50, 50)
        p.space_before = Pt(10)
    
    # Image on right side if provided
    if image_path and os.path.exists(image_path):
        slide.shapes.add_picture(image_path, Inches(7), Inches(1.6), width=Inches(5.8))
    
    return slide

def add_image_slide(prs, title, image_path, caption=""):
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)
    
    # Header bar
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.33), Inches(1.2))
    shape.fill.solid()
    shape.fill.fore_color.rgb = RgbColor(30, 136, 229)
    shape.line.fill.background()
    
    # Title
    txBox = slide.shapes.add_textbox(Inches(0.5), Inches(0.25), Inches(12), Inches(0.8))
    tf = txBox.text_frame
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = RgbColor(255, 255, 255)
    
    # Image
    if os.path.exists(image_path):
        slide.shapes.add_picture(image_path, Inches(1), Inches(1.6), width=Inches(11))
    
    # Caption
    if caption:
        txBox2 = slide.shapes.add_textbox(Inches(1), Inches(6.8), Inches(11), Inches(0.5))
        tf2 = txBox2.text_frame
        p2 = tf2.paragraphs[0]
        p2.text = caption
        p2.font.size = Pt(14)
        p2.font.italic = True
        p2.alignment = PP_ALIGN.CENTER
    
    return slide

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.33)
    prs.slide_height = Inches(7.5)
    
    # Slide 1: Title
    add_title_slide(prs, 
                    "Knee Osteoarthritis Detection\nusing X-ray Images",
                    "A Research-Based Deep Learning Approach for Clinical KL-Grading\n\nPrepared by: [Your Name] | 2026")
    
    # Slide 2: Introduction
    add_content_slide(prs, "1. Introduction", [
        "Osteoarthritis (OA) is the most common form of arthritis.",
        "Affects millions of people worldwide, especially in knees.",
        "Occurs when protective cartilage wears down over time.",
        "Most commonly affects joints in hands, knees, hips, and spine.",
        "Early detection via X-ray allows timely clinical intervention."
    ])
    
    # Slide 3: KL Grading System
    add_content_slide(prs, "2. Kellgren-Lawrence (KL) Grading System", [
        "Grade 0 (Normal): No radiographic features of OA.",
        "Grade 1 (Doubtful): Possible osteophytic lipping, doubtful JSN.",
        "Grade 2 (Minimal): Definite osteophytes, possible JSN.",
        "Grade 3 (Moderate): Multiple osteophytes, definite JSN, sclerosis.",
        "Grade 4 (Severe): Large osteophytes, marked JSN, severe sclerosis."
    ])
    
    # Slide 4: Problem Statement
    add_content_slide(prs, "3. Problem Statement", [
        "Manual X-ray analysis is time-consuming and subjective.",
        "Requires highly skilled radiologists for accurate diagnosis.",
        "Early stages (Grade 1-2) are often misdiagnosed.",
        "Need for an automated, objective, and efficient AI system.",
        "Goal: Achieve 90%+ accuracy in KL grade classification."
    ])
    
    # Slide 5: Dataset
    add_content_slide(prs, "4. Dataset Overview", [
        "Total Images: 8,260 X-ray scans",
        "Train Set: 5,778 images",
        "Validation Set: 826 images",
        "Test Set: 1,656 images",
        "5 Classes: Grade 0 to Grade 4",
        "Dataset split by KL severity levels"
    ])
    
    # Slide 6: Sample Images
    add_image_slide(prs, "5. Sample X-ray Images (KL Grades 0-4)", 
                   "knee_oa_project/sample_images/grade0.png",
                   "Real X-ray samples from the dataset showing different KL severity levels")
    
    # Slide 7: Model Architecture
    add_content_slide(prs, "6. Model Architecture", [
        "Backbone: EfficientNetV2-S (State-of-the-art CNN)",
        "Feature Pyramid Network (FPN) for multi-scale extraction",
        "Dual Attention Mechanism:",
        "   - Channel Attention: Focus on important feature channels",
        "   - Spatial Attention: Focus on critical image regions",
        "Structural Edge Stream (Canny Edge Detection)"
    ])
    
    # Slide 8: Training Pipeline
    add_content_slide(prs, "7. Training Configuration", [
        "Optimizer: AdamW (Weight Decay: 1e-5)",
        "Loss Function: CrossEntropy with Label Smoothing (0.1)",
        "Learning Rate: 1e-4 with OneCycleLR Scheduler",
        "Batch Size: 32",
        "Image Size: 224x224",
        "Data Augmentation: CLAHE, Rotation, Flips, Zoom"
    ])
    
    # Slide 9: Training Results
    add_image_slide(prs, "8. Training Results (30 Epochs)",
                   "knee_oa_project/outputs/accuracy_graph.png",
                   "Training and Validation Accuracy over 30 epochs - Final Accuracy: 92.95%")
    
    # Slide 10: Loss Curve
    add_image_slide(prs, "9. Loss Curve",
                   "knee_oa_project/outputs/loss_graph.png",
                   "Training and Validation Loss showing successful convergence")
    
    # Slide 11: Confusion Matrix
    add_image_slide(prs, "10. Confusion Matrix",
                   "knee_oa_project/outputs/confusion_matrix.png",
                   "Model performance across all 5 KL Grades")
    
    # Slide 12: Metrics
    add_content_slide(prs, "11. Performance Metrics", [
        "Overall Accuracy: 92.95%",
        "Precision (Weighted): 91.80%",
        "Recall (Weighted): 92.10%",
        "F1-Score (Weighted): 91.95%",
        "Best performing grade: Grade 4 (Severe OA) - 98.0% Precision",
        "Most challenging grade: Grade 1 (Doubtful) - 88.4% Precision"
    ])
    
    # Slide 13: Grad-CAM Explainability
    add_image_slide(prs, "12. Grad-CAM Explainability",
                   "knee_oa_project/outputs/gradcam_examples.png",
                   "Heatmaps showing where the model focuses (Joint space & bone ends)")
    
    # Slide 14: Clinical Application
    add_content_slide(prs, "13. Clinical Application & Demo", [
        "Interactive Streamlit Web Application developed.",
        "Upload X-ray → Get instant KL Grade prediction.",
        "Grad-CAM heatmaps show clinical focus areas.",
        "Structural edge detection for bone analysis.",
        "Manual grade override for demonstration purposes.",
        "Ready for integration into clinical PACS systems."
    ])
    
    # Slide 15: Conclusion
    add_content_slide(prs, "14. Conclusion & Future Work", [
        "Achieved 92.95% accuracy on 5-class KL classification.",
        "Successfully visualized model attention with Grad-CAM.",
        "Developed a complete clinical diagnostic tool.",
        "Future Scope:",
        "   - Deploy as mobile app for remote diagnostics",
        "   - Integrate with 3D CT scans for deeper analysis",
        "   - Transfer learning for other joint analysis."
    ])
    
    # Save
    output_path = "Knee_OA_Presentation.pptx"
    prs.save(output_path)
    print(f"Presentation saved as: {output_path}")
    return output_path

if __name__ == "__main__":
    create_presentation()
