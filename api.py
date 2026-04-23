from flask import Flask, request, jsonify

app = Flask(__name__)

API_KEY = "mysecret123"

# Health check
@app.route("/api/v1/health")
def health():
    return jsonify({"status": "ok"})

# Example: get data
@app.route("/api/v1/data", methods=["GET"])
def get_data():
    key = request.headers.get("x-api-key")
    if key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 403
    
    return jsonify({
        "success": True,
        "message": "API working properly"
    })

# Example: post data
@app.route("/api/v1/data", methods=["POST"])
def post_data():
    key = request.headers.get("x-api-key")
    if key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 403
    
    data = request.json
    return jsonify({
        "success": True,
        "received": data
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
