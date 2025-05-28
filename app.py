from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route("/verificar", methods=["GET"])
def verificar_id():
    id_recebido = request.args.get("id")
    with open("ids_autorizados.json") as f:
        ids = json.load(f)
    if id_recebido in ids:
        return jsonify({"autorizado": True})
    else:
        return jsonify({"autorizado": False})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
