from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/payment/process', methods=['POST'])
def process_payment():
    data = request.get_json()
    order_id = data.get('order_id')
    amount = data.get('amount')

    # Process payment logic goes here

    return jsonify({"message": "Payment processed successfully"})

if __name__ == '__main__':
    app.run(debug=True)
