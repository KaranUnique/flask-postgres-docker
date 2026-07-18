from app.repositories.postgres_repository import PostgresRepository

repo = PostgresRepository()


class StudentService:

    def get_students(self):
        return repo.get_all()

    def get_student(self, student_id):
        return repo.get_by_id(student_id)

    def create_student(self, data):
        return repo.create(data)

    def update_student(self, student_id, data):
        return repo.update(student_id, data)

    def delete_student(self, student_id):
        repo.delete(student_id)