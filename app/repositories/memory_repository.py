class MemoryRepository:

    def __init__(self):
        self.students = []
        self.next_id = 1

    def get_all(self):
        return self.students

    def get_by_id(self, student_id):
        for student in self.students:
            if student["id"] == student_id:
                return student
        return None

    def create(self, student):

        student["id"] = self.next_id
        self.next_id += 1

        self.students.append(student)

        return student

    def update(self, student_id, data):

        student = self.get_by_id(student_id)

        if not student:
            return None

        student["name"] = data["name"]
        student["age"] = data["age"]
        student["course"] = data["course"]

        return student

    def delete(self, student_id):

        student = self.get_by_id(student_id)

        if not student:
            return False

        self.students.remove(student)

        return True