@app.route("/api/db-test")
def db_test():
    try:
        # Apenas simular resposta
        return jsonify({"db_status": "instanciado"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

