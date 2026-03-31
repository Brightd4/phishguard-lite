# PhishGuard Lite

## Demo

![App Screenshot](screenshots/app.png)

PhishGuard Lite is a lightweight, interpretable phishing detection and risk scoring framework designed for practical email and message security analysis.

It combines rule-based detection with transparent scoring to provide clear explanations of why a message is considered suspicious.

---

## Overview

Phishing attacks remain one of the most common cybersecurity threats, often relying on deceptive language, malicious links, and urgency cues.

PhishGuard Lite addresses this problem using a rule-based approach that prioritizes:

- Interpretability
- Simplicity
- Lightweight deployment
- Real-time analysis capability

Unlike black-box models, this system provides clear reasoning behind every detection decision.

---

## Key Features

- Rule-based phishing detection
- Risk scoring and classification (Low, Medium, High)
- Detection of suspicious keywords and domains
- Explainable output with identified triggers
- Lightweight Flask-based web interface
- Real-time analysis of user input

---

## How It Works

PhishGuard Lite analyzes input text (emails or messages) using predefined phishing indicators such as:

- Suspicious keywords (e.g., "urgent", "verify", "account suspended")  
- Presence of suspicious links or domains  
- Request for sensitive information  
- Social engineering patterns  

Each detected signal contributes to a cumulative **risk score**, which determines whether the message is:

- Safe  
- Suspicious  
- High Risk  

The system also provides explanations for each decision, making it suitable for real-world use cases where transparency is required.

---
## 🖥️ System Architecture

The system consists of:

- Input processing module  
- Rule-based detection engine  
- Risk scoring component  
- Explanation generator  
- Flask web interface  

## Installation

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

## 📊 Example Output

Input:
