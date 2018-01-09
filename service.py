from flask import Flask, request, jsonify
from predictor import Predictor

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def score():
    data = request.get_json(force=True)
    
    score = Predictor().predict(data)
    
    return jsonify(results=score)

if __name__ == '__main__':
    app.run(port=3000)