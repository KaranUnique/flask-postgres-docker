from app.repositories.repository import repository


class StudentService:

    def get_students(self):
        return repository.get_all()

    def get_student(self, student_id):
        return repository.get_by_id(student_id)

    def create_student(self, data):
        return repository.create(data)

    def update_student(self, student_id, data):
        return repository.update(student_id, data)

    def delete_student(self, student_id):
        return repository.delete(student_id)