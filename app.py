from flask import Flask, jsonify
from flask_cors import CORS
import random
import time

app = Flask(__name__)
CORS(app)

prices = {
    "AZUL4F": 27.42,
    "PETR4": 81.5,
}

historical_data = {
    "AZUL4F": [],
    "PETR4": []
}


def generate_market_data(price):
    spread = round(random.uniform(0.01, 0.05), 4)
    bid = round(price - spread / 2, 4)
    ask = round(price + spread / 2, 4)
    volume = random.randint(100, 10000)

    return bid, ask, spread, volume


@app.route('/metatrader5/market-data/<symbol>', methods=['GET'])
def get_market_data(symbol):
    global prices

    if symbol not in prices:
        return jsonify({"error": "Invalid symbol"}), 404

    variation = random.uniform(-1, 1)
    prices[symbol] = round(prices[symbol] + variation, 4)

    bid, ask, spread, volume = generate_market_data(prices[symbol])

    timestamp = int(time.time() * 1000)

    historical_data[symbol].append(
        {
            'price': prices[symbol],
            'bid': bid,
            'ask': ask,
            'spread': spread,
            'volume': volume,
            'timestamp': timestamp
        }
    )

    return jsonify({
        'symbol': symbol,
        'price': prices[symbol],
        'bid': bid,
        'ask': ask,
        'spread': spread,
        'volume': volume,
        'timestamp': timestamp
    })


@app.route('/metatrader5/historical-data/<symbol>', methods=['GET'])
def get_historical_data(symbol):
    if symbol not in historical_data:
        return jsonify({"error": "Invalid symbol"}), 404

    return jsonify(historical_data[symbol])


if __name__ == '__main__':
    app.run(debug=True)
