# Fusion of Emotional State for Robust Personality Prediction 🎭🤖

Welcome to the repository for the **Multimodal Emotion and Personality Recognition System**! This project integrates state-of-the-art deep learning techniques across text, audio, and video modalities to accurately recognize human emotions and infer personality traits in real-time. Perfect for applications in HR, mental health, and human-computer interaction (HCI).

## 🚀 Project Overview

Understanding human emotions and personality is crucial for creating empathetic AI systems. This project builds a **real-time multimodal AI framework** that fuses emotional cues from speech, text, and facial expressions to classify eight core emotions with over **90% accuracy**. Beyond emotion recognition, it maps emotional patterns to the **Big Five personality traits** using a novel rule-based heuristic system.

## 🧠 Key Features

- **Multimodal Emotion Recognition:**  
  Utilizes **BERT** for text, **CNN-LSTM** for audio, and **ResNet50 + MLP** for video to extract rich emotional features.

- **Confidence-Based Fusion:**  
  Combines predictions from all three modalities using a confidence-weighted voting mechanism to improve robustness and accuracy.

- **Personality Trait Inference:**  
  Implements a rule-based system that analyzes sequences of predicted emotions to infer the Big Five personality traits: Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism.

- **Real-Time CPU Optimization:**  
  Models are optimized to run efficiently on CPUs, enabling deployment in resource-constrained environments without GPU dependency.

- **Dataset:**  
  Trained and evaluated on the **IEMOCAP dataset** from USC, containing over **12 hours of synchronized audiovisual data** across **14,792 utterances**.

## 🎯 Why This Project?

Emotion recognition from a single modality often suffers from ambiguity and noise. By fusing multiple data sources, this system captures complementary information, leading to more accurate and reliable emotion classification. Mapping emotions to personality traits opens avenues for personalized AI applications, such as adaptive virtual assistants, mental health monitoring, and talent assessment in HR.

## 🛠️ Technologies Used

- **Languages & Frameworks:** Python, PyTorch, TensorFlow, Scikit-learn  
- **NLP:** Hugging Face Transformers (BERT)  
- **Computer Vision:** OpenCV, ResNet50 pretrained models  
- **Audio Processing:** CNN-LSTM architectures for Mel-frequency features  
- **APIs:** Assembly.ai for speech-to-text preprocessing  
- **Data:** IEMOCAP multimodal emotional dataset


