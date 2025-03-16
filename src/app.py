from flask import Flask
import os


app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, world! This is a Flask app running with CI/CD."


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Use PORT from environment or default to 5000
    app.run(host="127.0.0.1", port=port) 