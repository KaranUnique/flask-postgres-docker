class Student:
    def __init__(self, id, name, age, course):
        self.id = id
        self.name = name
        self.age = age
        self.course = course

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "course": self.course
        }