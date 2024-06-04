from flask import Flask, jsonify
from flask_cors import CORS
import random
import time

app = Flask(__name__)
CORS(app)

current_price = 90.0


@app.route('/market-data', methods=['GET'])
def get_market_data():
    global current_price

    variation = random.uniform(-1, 1)
    current_price = round(current_price + variation, 2)
    timestamp = int(time.time() * 1000)

    return jsonify({'price': current_price, 'timestamp': timestamp})


if __name__ == '__main__':
    app.run(debug=True)
