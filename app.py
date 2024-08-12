from flask import Flask, jsonify
from flask_cors import CORS
import random
import time

app = Flask(__name__)
CORS(app)

prices = {
    "AZUL4F": 81.0,
    "PETR4": 27.5,
}

historical_data = {
    "AZUL4F": [],
    "PETR4": []
}


@app.route('/market-data/<symbol>', methods=['GET'])
def get_market_data(symbol):
    global prices

    if symbol not in prices:
        return jsonify({"error": "Invalid symbol"}), 404

    variation = random.uniform(-1, 1)
    prices[symbol] = round(prices[symbol] + variation, 2)
    timestamp = int(time.time() * 1000)

    historical_data[symbol].append(
        {'price': prices[symbol], 'timestamp': timestamp}
        )

    return jsonify(
        {'symbol': symbol, 'price': prices[symbol], 'timestamp': timestamp}
        )


@app.route('/historical-data/<symbol>', methods=['GET'])
def get_historical_data(symbol):
    if symbol not in historical_data:
        return jsonify({"error": "Invalid symbol"}), 404

    return jsonify(historical_data[symbol])


if __name__ == '__main__':
    app.run(debug=True)
