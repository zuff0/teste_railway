from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from models.database import Database
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

db = Database()

@app.route("/api/health")
def health():
    return jsonify({
        "status": "ok",
        "env_check": os.getenv("TEST_VAR", "não definido")
    })

@app.route("/api/db-test")
def db_test():
    try:
        # Usa método ping() do banco só pra testar se tá importado
        result = db.ping()
        return jsonify({"db_status": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

