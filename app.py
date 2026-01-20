from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def health():
    return jsonify({
        "status": "ok",
        "service": "faklartsvar-api",
        "message": "API is running"
    })

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(silent=True) or {}
    question = data.get("question", "").strip()

    if not question:
        return jsonify({"error": "No question provided"}), 400

    # Midlertidig placeholder-svar (AI kobles på senere)
    return jsonify({
        "question": question,
        "answer": "Dette er et midlertidig svar. AI kobles på i neste steg."
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
