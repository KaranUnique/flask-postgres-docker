from flask import Blueprint, jsonify, request

from app.services.student_service import StudentService

student_bp = Blueprint("students", __name__)

service = StudentService()


@student_bp.route("/students", methods=["GET"])
def get_students():
    return jsonify(service.get_students())


@student_bp.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):

    student = service.get_student(student_id)

    if student is None:
        return jsonify({"message": "Student not found"}), 404

    return jsonify(student)


@student_bp.route("/students", methods=["POST"])
def create_student():

    data = request.get_json()

    if not data:
        return jsonify({"message": "Request body is required"}), 400

    required_fields = ["name", "age", "course"]

    for field in required_fields:
        if field not in data:
            return jsonify({"message": f"{field} is required"}), 400

    student = service.create_student(data)

    return jsonify(student), 201


@student_bp.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):

    data = request.get_json()

    if not data:
        return jsonify({"message": "Request body is required"}), 400

    student = service.update_student(student_id, data)

    if student is None:
        return jsonify({"message": "Student not found"}), 404

    return jsonify(student)


@student_bp.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):

    deleted = service.delete_student(student_id)

    if not deleted:
        return jsonify({"message": "Student not found"}), 404

    return jsonify({"message": "Student deleted successfully"})