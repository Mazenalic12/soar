from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ SOAR System is running on Google Cloud VM!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
