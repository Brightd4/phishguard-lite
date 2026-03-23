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
        "update your payment"
    ]

    suspicious_domains = [
        "bit.ly",
        "tinyurl",
        "secure-update",
        "account-verify",
        "free-login"
    ]

    lower_text = text.lower()

    for keyword in suspicious_keywords:
        if keyword in lower_text:
            score += 1
            triggers.append(keyword)

    for domain in suspicious_domains:
        if domain in lower_text:
            score += 2
            triggers.append(domain)

    if "http://" in lower_text:
        score += 1
        triggers.append("http link")

    if "@" in lower_text:
        score += 1
        triggers.append("@ symbol")

    if score >= 5:
        risk = "High"
    elif score >= 3:
        risk = "Medium"
    else:
        risk = "Low"

    return {
        "score": score,
        "risk": risk,
        "triggers": triggers
    }