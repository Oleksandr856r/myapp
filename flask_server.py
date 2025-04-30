from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello')
def hello():
    return jsonify({"message": "Привіт з Flask!"})

def run_flask():
    app.run(host="0.0.0.0", port=8000, debug=False, use_reloader=False)
