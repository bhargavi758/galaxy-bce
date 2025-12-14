from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"


@app.route("/health")
def health():
    """Health check endpoint for Kubernetes liveness/readiness probes"""
    return {"status": "healthy"}, 200


@app.route("/api/dummy")
def dummy():
    """Dummy API endpoint"""
    return {
        "message": "This is a dummy endpoint",
        "service": "galaxy-bce",
        "version": os.getenv("APP_VERSION", "1.0.0")
    }, 200


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)