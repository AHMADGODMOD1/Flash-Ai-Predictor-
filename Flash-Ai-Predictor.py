from flask import Flask, request, jsonify

app = Flask(__name__)

def ai_predict(history):
    """
    AI-based prediction using trend analysis.
    - If 'Big' occurrences > 'Small', predict 'Big'
    - If 'Small' occurrences > 'Big', predict 'Small'
    - If equal, choose based on weighted probability
    """
    if not history:
        return "No Data"

    big_count = sum(1 for item in history if item["number"] > 4)
    small_count = len(history) - big_count

    big_probability = big_count / len(history)
    small_probability = small_count / len(history)

    if big_probability > small_probability:
        return "Big"
    elif small_probability > big_probability:
        return "Small"
    else:
        return "Big" if big_probability > 0.5 else "Small"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json.get("history", [])
        prediction = ai_predict(data)
        return jsonify({"prediction": prediction})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)