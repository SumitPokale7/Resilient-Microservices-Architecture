from flask import Flask, jsonify

app = Flask(__name__)

orders = [
    {"id": 1, "user_id": 1, "total": 50},
    {"id": 2, "user_id": 2, "total": 30},
    {"id": 3, "user_id": 3, "total": 40}
]

@app.route('/orders')
def get_orders():
    return jsonify(orders)

@app.route('/orders/<int:order_id>')
def get_order(order_id):
    order = next((order for order in orders if order['id'] == order_id), None)
    if order:
        return jsonify(order)
    else:
        return jsonify({"error": "Order not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
