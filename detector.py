import joblib
from pathlib import Path

# =========================
# LOAD MODEL + VECTORIZER
# =========================

BASE_DIR = Path(__file__).resolve().parent

model_path = BASE_DIR / "models" / "phishguard_logistic_model.pkl"
vectorizer_path = BASE_DIR / "models" / "phishguard_tfidf_vectorizer.pkl"

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)


# =========================
# MAIN ANALYSIS FUNCTION
# =========================

def analyze_input(text: str) -> dict:

    score = 0
    triggers = []

    suspicious_keywords = [
        "verify your account",
        "urgent action required",
        "click here",
        "login immediately",
        "password reset",
        "bank alert",
        "confirm identity",
        "suspended account",
        "security notice",
        "update your payment",
        "account suspended",
        "verify now",
        "limited time",
        "act immediately",
        "confirm your account"
    ]

    suspicious_domains = [
        "bit.ly",
        "tinyurl",
        "secure-update",
        "account-verify",
        "free-login"
    ]

    lower_text = text.lower()

    # =========================
    # RULE BASED DETECTION
    # =========================

    for keyword in suspicious_keywords:
        if keyword in lower_text:
            score += 1
            triggers.append(keyword)

    for domain in suspicious_domains:
        if domain in lower_text:
            score += 2
            triggers.append(domain)

    if "http://" in lower_text or "https://" in lower_text or "www." in lower_text:
        score += 1
        triggers.append("link detected")

    if "@" in lower_text:
        score += 1
        triggers.append("@ symbol")

    # =========================
    # AI MODEL DETECTION
    # =========================

    transformed_text = vectorizer.transform([text])

    ai_prediction = model.predict(transformed_text)[0]
    ai_probability = model.predict_proba(transformed_text)[0][1]

    if ai_prediction == 1:
        score += 2
        triggers.append("AI_MODEL_FLAG")

    elif ai_probability >= 0.30:
        score += 1
        triggers.append("AI_SUSPICION_SIGNAL")

    # =========================
    # RISK CLASSIFICATION
    # =========================

    if score >= 5:
        risk = "High"
    elif score >= 3:
        risk = "Medium"
    else:
        risk = "Low"

    return {
        "score": score,
        "risk": risk,
        "triggers": triggers,
        "ai_prediction": int(ai_prediction),
        "ai_confidence": round(float(ai_probability), 3)
    }