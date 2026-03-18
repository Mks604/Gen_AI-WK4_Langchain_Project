from flask import Flask, render_template, request, jsonify
from utils import generate_email

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt")
    tone = data.get("tone")

    email = generate_email(prompt, tone)
    return jsonify({"email": email})

if __name__ == "__main__":
    app.run(debug=True)