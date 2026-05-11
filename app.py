from flask import Flask, request, jsonify
from flask_cors import CORS
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
CORS(app)
analyzer = SentimentIntensityAnalyzer()

KEYWORDS = {
    "Pricing & Labor": ["price", "charge", "cost", "overcharge", "expensive", "quote", "bill", "labor", "fee"],
    "Communication Issues": ["call", "never", "back", "update", "told", "know", "response", "wait", "ignored"],
    "Brake & Repair Quality": ["brake", "repair", "fix", "return", "same", "problem", "issue", "broke", "quality"],
    "Oil Change Problems": ["oil", "change", "filter", "engine", "light", "leak", "synthetic"]
}

def predict_category(text):
    text_lower = text.lower()
    scores = {}
    for category, words in KEYWORDS.items():
        scores[category] = sum(1 for word in words if word in text_lower)
    return max(scores, key=scores.get)

@app.route("/")
def home():
    return jsonify({"status": "running", "service": "Auto Repair Sentiment API"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or "review" not in data:
        return jsonify({"error": "Please provide a review field"}), 400
    review = data["review"]
    sentiment = analyzer.polarity_scores(review)
    category = predict_category(review)
    return jsonify({
        "review": review,
        "sentiment_score": sentiment["compound"],
        "sentiment_label": "positive" if sentiment["compound"] > 0 else "negative",
        "predicted_category": category
    })

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))