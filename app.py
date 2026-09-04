from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    app.logger.info("Home endpoint was accessed")
    return "Hello from Python DevOps App!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)