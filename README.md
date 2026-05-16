# PhishGuard Lite

A Lightweight Hybrid Explainable Phishing Detection System Using Rule Based Analysis and Machine Learning

---
## Live Demo

https://phishguard-lite-2.onrender.com

---
## Demo

![App Screenshot](screenshots/app.png)

---

## Overview

PhishGuard Lite is a lightweight hybrid phishing detection framework designed to identify suspicious emails, SMS messages, and phishing related text using a combination of rule based analysis and machine learning classification.

The system combines transparent heuristic detection with a TF IDF + Logistic Regression machine learning model to improve phishing detection while maintaining explainability and low computational overhead.

Unlike many black box cybersecurity systems, PhishGuard Lite provides interpretable explanations showing why a message was flagged as suspicious.

---
## Research Motivation

Phishing attacks remain one of the most common cybersecurity threats affecting individuals and organizations worldwide. Many existing phishing detection systems rely on black box machine learning models that provide limited interpretability.

PhishGuard Lite was developed as a lightweight explainable phishing detection framework that combines rule based analysis with machine learning classification to improve transparency, interpretability, and accessibility for educational and research purposes.

---
## Key Features

- Hybrid phishing detection using rule based analysis and machine learning
- Lightweight Logistic Regression phishing classifier
- TF IDF feature extraction pipeline
- Risk scoring and classification
- Explainable detection output
- Detection of suspicious keywords and phishing domains
- Real time Flask web application
- Fast inference suitable for lightweight deployment
- Human interpretable trigger explanations

---

## System Architecture

The system consists of the following major components:

- Input Processing Module
- Rule Based Detection Engine
- TF IDF Feature Extraction Module
- Machine Learning Classification Engine
- Risk Scoring and Fusion Layer
- Explainability Engine
- Flask Web Interface

![PhishGuard Lite Architecture](screenshots/phishguard_architecture.png)

---

## How It Works

PhishGuard Lite analyzes text messages using two complementary approaches.

### Rule Based Detection

The rule based engine searches for suspicious phishing indicators including:

- Urgency related phrases
- Account verification requests
- Suspicious links
- Credential harvesting patterns
- Social engineering indicators
- Suspicious domains

Each detected trigger contributes to a cumulative phishing risk score.

### Machine Learning Detection

The machine learning module uses:

- TF IDF vectorization
- Logistic Regression classification

The model was trained using the SMS Spam Collection dataset and contributes an additional AI based phishing confidence signal.

### Hybrid Risk Assessment

The final risk level combines:

- Rule based trigger scoring
- AI prediction confidence
- Suspicious link analysis

The system outputs:

- Risk Score
- Risk Level
- Detected Triggers
- AI Prediction
- AI Confidence
- Human readable explanation

---
## Limitations

Current limitations of the system include:

- Limited phishing keyword coverage
- Lightweight machine learning model
- English only detection
- No real time URL reputation analysis
- Limited adversarial robustness
- Small scale deployment environment

Future work will focus on transformer based phishing detection, multilingual support, and improved threat intelligence integration.

---
## Technologies Used

- Python
- Flask
- Scikit learn
- Pandas
- NumPy
- Joblib
- HTML/CSS
- JavaScript

---

## Dataset

The machine learning component of PhishGuard Lite was trained using the publicly available SMS Spam Collection dataset.

Dataset source:

https://archive.ics.uci.edu/dataset/228/sms+spam+collection

The original dataset contains SMS messages labeled as either legitimate messages or spam messages. For this project, the labels were converted into numerical form:

- 0 = legitimate message
- 1 = suspicious or phishing related message

The raw dataset file was placed in:

```text
datasets/raw/SMSSpamCollection

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Brightd4/phishguard-lite.git
cd phishguard-lite

python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt

python app.py

---
## How to Use

### 1. Open the Live Demo

Visit the deployed application below:

https://phishguard-lite-2.onrender.com

### 2. Paste a Suspicious Message

Example phishing message:

```text
Urgent action required. Your account has been suspended. Click here to verify your account immediately: http://secure-update-login.com

---
## Citation

If you use this project in research or educational work, please cite:

Duffour, B. (2026). PhishGuard Lite: A Lightweight Explainable Phishing Detection System.
