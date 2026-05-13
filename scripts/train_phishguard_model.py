import pandas as pd
import joblib
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)

# Load dataset
df = pd.read_csv("../datasets/processed/sms_spam.csv")

# Features and labels
X = df["text"].astype(str)
y = df["label"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# TF-IDF vectorizer
vectorizer = TfidfVectorizer(
    stop_words="english",
    lowercase=True,
    max_features=5000,
    ngram_range=(1, 2)
)

# Transform text
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Logistic Regression model
model = LogisticRegression(max_iter=1000)

# Train model
model.fit(X_train_tfidf, y_train)

# Predictions
y_pred = model.predict(X_test_tfidf)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("\nPhishGuard Model Evaluation Results")
print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1 Score:  {f1:.4f}")

print("\nClassification Report")
print(classification_report(y_test, y_pred))

# Create models folder
model_dir = Path("../models")
model_dir.mkdir(parents=True, exist_ok=True)

# Save model and vectorizer
joblib.dump(model, model_dir / "phishguard_logistic_model.pkl")
joblib.dump(vectorizer, model_dir / "phishguard_tfidf_vectorizer.pkl")

print("\nSaved model to:", model_dir / "phishguard_logistic_model.pkl")
print("Saved vectorizer to:", model_dir / "phishguard_tfidf_vectorizer.pkl")