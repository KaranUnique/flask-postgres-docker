from flask import Blueprint, jsonify, request

from app.services.student_service import StudentService

student_bp = Blueprint("students", __name__)

service = StudentService()


@student_bp.route("/students", methods=["GET"])
def get_students():
    return jsonify(service.get_students())


@student_bp.route("/students/<int:id>", methods=["GET"])
def get_student(id):

    student = service.get_student(id)

    if student:
        return jsonify(student)

    return jsonify({"message": "Student not found"}), 404


@student_bp.route("/students", methods=["POST"])
def create_student():

    student = service.create_student(request.json)

    return jsonify(student), 201


@student_bp.route("/students/<int:id>", methods=["PUT"])
def update_student(id):

    student = service.update_student(id, request.json)

    return jsonify(student)


@student_bp.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):

    service.delete_student(id)

    return jsonify({
        "message": "Student deleted"
    })