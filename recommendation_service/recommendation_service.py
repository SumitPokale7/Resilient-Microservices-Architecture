from flask import Flask, jsonify

app = Flask(__name__)

recommendations = {
    1: ["Book A", "Book B", "Book C"],
    2: ["Book X", "Book Y", "Book Z"],
    3: ["Book M", "Book N", "Book O"]
}

@app.route('/recommendations/<int:user_id>')
def get_recommendations(user_id):
    if user_id in recommendations:
        return jsonify(recommendations[user_id])
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
