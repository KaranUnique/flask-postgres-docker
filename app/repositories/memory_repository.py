students = []
next_id = 1


class MemoryRepository:

    def get_all(self):
        return students

    def get_by_id(self, student_id):
        for s in students:
            if s["id"] == student_id:
                return s
        return None

    def create(self, student):
        global next_id

        student["id"] = next_id
        next_id += 1

        students.append(student)
        return student

    def update(self, student_id, data):
        student = self.get_by_id(student_id)

        if student:
            student.update(data)
            return student

        return None

    def delete(self, student_id):
        global students

        students = [s for s in students if s["id"] != student_id]