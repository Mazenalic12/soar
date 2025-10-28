from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ SOAR System is running on Google Cloud VM!"

# ✅ Nieuw endpoint om alerts te ontvangen van Snort
@app.route('/event', methods=['POST'])
def event():
    data = request.get_json()
    print("🚨 Received alert from Snort:", data)
    return jsonify({"status": "received"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
