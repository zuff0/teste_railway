from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from models.database import Database

# Inicializar (não precisa abrir conexão ainda)
db = Database()


# Carregar variáveis de ambiente do .env
load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route("/api/health")
def health():
    return jsonify({
        "status": "ok",
        "env_check": os.getenv("TEST_VAR", "não definido")
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

