import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world! This is a Flask app running with CI/CD."

if __name__ == "__main__":
    host = os.environ.get("FLASK_RUN_HOST", "0.0.0.0")  # Default to 0.0.0.0
    port = int(os.environ.get("PORT", 8080))  
    app.run(host=host, port=port)