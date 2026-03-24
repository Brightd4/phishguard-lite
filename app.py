from flask import Flask, request, render_template_string, jsonify
import os

app = Flask(__name__)

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

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>PhishGuard Lite</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f7fb;
            margin: 0;
            padding: 0;
            color: #1f2937;
        }

        .container {
            max-width: 800px;
            margin: 40px auto;
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.08);
        }

        h1 {
            margin-top: 0;
            color: #0f172a;
        }

        textarea {
            width: 100%;
            height: 160px;
            padding: 12px;
            font-size: 15px;
            border: 1px solid #cbd5e1;
            border-radius: 8px;
            box-sizing: border-box;
            resize: vertical;
        }

        button {
            margin-top: 15px;
            padding: 12px 20px;
            background: #2563eb;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 15px;
        }

        button:hover {
            background: #1d4ed8;
        }

        .result {
            margin-top: 25px;
            padding: 20px;
            border-radius: 10px;
            background: #f8fafc;
            border: 1px solid #e2e8f0;
        }

        .high {
            color: #b91c1c;
            font-weight: bold;
        }

        .medium {
            color: #b45309;
            font-weight: bold;
        }

        .low {
            color: #15803d;
            font-weight: bold;
        }

        ul {
            margin-top: 10px;
            padding-left: 20px;
        }

        .footer {
            margin-top: 24px;
            font-size: 13px;
            color: #64748b;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>PhishGuard Lite</h1>
        <p>A lightweight phishing risk detector for suspicious messages and links.</p>

        <form method="POST">
            <textarea name="text" placeholder="Paste suspicious email text, message, or link here...">{{ submitted_text or "" }}</textarea>
            <br>
            <button type="submit">Analyze</button>
        </form>

        {% if result %}
        <div class="result">
            <p>Risk Level:
                <span class="{{ result['risk'].lower() }}">{{ result['risk'] }}</span>
            </p>
            <p>Risk Score: {{ result['score'] }}</p>
            <p>Triggers Found:</p>

            {% if result['triggers'] %}
                <ul>
                    {% for trigger in result['triggers'] %}
                        <li>{{ trigger }}</li>
                    {% endfor %}
                </ul>
            {% else %}
                <p>No suspicious triggers found.</p>
            {% endif %}
        </div>
        {% endif %}

        <div class="footer">
            Health check available at /health
        </div>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    submitted_text = ""

    if request.method == "POST":
        submitted_text = request.form.get("text", "")
        result = analyze_input(submitted_text)

    return render_template_string(
        HTML_TEMPLATE,
        result=result,
        submitted_text=submitted_text
    )

@app.route("/health")
def health():
    return "ok", 200

@app.route("/api/analyze", methods=["POST"])
def api_analyze():
    data = request.get_json(silent=True)

    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' field"}), 400

    result = analyze_input(data["text"])
    return jsonify(result)

# This is important for Render - the application object should be named 'app'
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)