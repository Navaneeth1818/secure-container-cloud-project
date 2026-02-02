from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "Secure container app is running!"

if __name__ == "__main__":
    print("Starting Flask app on port 8080...")
    app.run(host="0.0.0.0", port=8080)

