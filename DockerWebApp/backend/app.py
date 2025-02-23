from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    return jsonify({"message": "Bienvenue dans l'API Flask déployée avec Docker !"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
