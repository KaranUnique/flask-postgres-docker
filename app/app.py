from flask import Flask

from app.routes.student_routes import student_bp

app = Flask(__name__)

app.register_blueprint(student_bp)


@app.route("/")
def home():
    return {
        "message": "Student Management API",
        "status": "Running"
    }


@app.route("/health")
def health():
    return {
        "status": "healthy"
    }


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )