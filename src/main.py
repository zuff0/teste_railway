from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/api/health", methods=['GET'])
def health():
    return jsonify({"status": "ok"})

# Só pra debug em ambiente Railway:
@app.route("/")
def hello():
    return "Backend vivo na raiz também!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

