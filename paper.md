---
title: 'PhishGuard Lite: A Lightweight Explainable Phishing Detection System'
tags:
  - Python
  - cybersecurity
  - phishing detection
  - explainable AI
  - machine learning
  - natural language processing
authors:
  - name: Bright Duffour
    orcid: 0009-0001-3763-5654
    affiliation: 1
affiliations:
  - name: University of the Potomac
    index: 1
date: 13 May 2026
bibliography: paper.bib
---

# Summary

PhishGuard Lite is a lightweight explainable phishing detection system designed to analyze suspicious emails, SMS messages, and phishing related text. The software combines rule based detection with a machine learning classifier using TF IDF feature extraction and Logistic Regression. The system provides phishing risk scores, detected triggers, AI confidence values, and human readable explanations to support transparent cybersecurity decision making.

# Statement of need

Phishing remains one of the most common cybersecurity threats affecting individuals, organizations, and digital communication systems. Many phishing detection tools rely on opaque models that provide limited explanation for their predictions. This creates challenges for users, educators, and security analysts who need to understand why a message is considered suspicious.

PhishGuard Lite addresses this need by providing a lightweight and interpretable phishing analysis framework. The system is designed for practical use in cybersecurity education, early threat analysis, research prototyping, and explainable AI demonstrations. It is especially useful for users who need a transparent phishing detection tool that can run with modest computational resources.

# Functionality

PhishGuard Lite provides the following functionality:

- detection of suspicious phishing keywords and phrases
- identification of suspicious links and domains
- hybrid rule based and machine learning risk scoring
- TF IDF and Logistic Regression based classification
- AI confidence reporting
- interpretable trigger explanations
- Flask based web interface
- lightweight deployment support

The software can be used to test suspicious messages, demonstrate explainable cybersecurity principles, and support reproducible experimentation with phishing related text classification.

# Research and software context

PhishGuard Lite is related to prior work in SMS spam filtering, phishing detection, and explainable artificial intelligence. The machine learning component uses the SMS Spam Collection dataset introduced by Almeida et al. [@almeida2011sms]. The system also builds on the broader need for interpretable machine learning discussed by Doshi Velez and Kim [@doshi2017interpretable] and explainable AI survey work by Adadi and Berrada [@adadi2018xai].

Unlike large black box systems, PhishGuard Lite emphasizes lightweight deployment, transparent scoring, and human readable explanations. This makes it suitable for research software demonstrations, cybersecurity education, and practical prototyping.

# Availability

The software is available on GitHub at:

https://github.com/Brightd4/phishguard-lite

The archived software release is available through Zenodo:

https://doi.org/10.5281/zenodo.20159815

# Acknowledgements

This software was developed as part of ongoing doctoral research in explainable AI, cybersecurity, and trustworthy detection systems.

# References