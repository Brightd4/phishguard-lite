from flask import Flask, request, render_template_string, jsonify
from detector import analyze_input
import os

app = Flask(__name__)

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

        .card {
            background: white;
            border: 1px solid #e5e7eb;
            border-radius: 10px;
            padding: 14px;
            margin-top: 14px;
        }

        .label {
            font-weight: bold;
            color: #0f172a;
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
        <p>A lightweight hybrid phishing risk detector for suspicious messages and links.</p>

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

            <div class="card">
                <p><span class="label">AI Prediction:</span>
                    {% if result['ai_prediction'] == 1 %}
                        Potential Phishing
                    {% else %}
                        Likely Safe
                    {% endif %}
                </p>

                <p><span class="label">AI Confidence:</span> {{ result['ai_confidence'] }}</p>
            </div>

            <div class="card">
                <p class="label">Triggers Found:</p>

                {% set clean_triggers = [] %}
                {% for trigger in result['triggers'] %}
                    {% if not trigger.startswith("AI_") %}
                        {% set _ = clean_triggers.append(trigger) %}
                    {% endif %}
                {% endfor %}

                {% if clean_triggers %}
                    <ul>
                        {% for trigger in clean_triggers %}
                            <li>{{ trigger }}</li>
                        {% endfor %}
                    </ul>
                {% else %}
                    <p>No rule-based triggers found.</p>
                {% endif %}
            </div>

            <div class="card">
                <p class="label">Explanation:</p>

                {% if result['triggers'] %}
                    {% if result['ai_prediction'] == 1 or "AI_SUSPICION_SIGNAL" in result['triggers'] %}
                        <p>
                            The analysis identified phishing indicators in the message.
                            The final risk assessment reflects a combination of rule-based detection
                            and machine learning inference.
                        </p>
                    {% else %}
                        <p>
                            The analysis identified phishing indicators based on rule-based detection.
                        </p>
                    {% endif %}
                {% else %}
                    <p>
                        No strong phishing indicators were detected in the message.
                    </p>
                {% endif %}
            </div>
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
        submitted_text = request.form.get("text", "").strip()

        if submitted_text:
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

    user_text = data["text"].strip()

    if not user_text:
        return jsonify({"error": "Text cannot be empty"}), 400

    result = analyze_input(user_text)
    return jsonify(result)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)