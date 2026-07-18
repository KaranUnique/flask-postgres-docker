from flask import Flask

from app.routes.student_routes import student_bp

app = Flask(__name__)

app.register_blueprint(student_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)