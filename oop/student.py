from oop.base import TimestampMixin
from oop.person import Person, person_pesho


class Student(TimestampMixin, Person):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.occupation = "Student"
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def custom_method(self):
        print("Student has no custom methods yet")

    @classmethod
    def create_from_person(cls, person_instance):
        return cls(
            person_instance.gender,
            person_instance.age,
            person_instance.height,
            person_instance.weight,
            person_instance.name,
        )


student_one = Student.create_from_person(person_pesho)
print(student_one, f"I am {student_one.occupation}")
print(student_one.name, student_one.age)

student_one.add_course(
    {
        "name": "Math",
        "credits": 12,
        "length": "12 weeks",
    }
)

print(student_one.courses)

person_pesho.custom_method()
student_one.custom_method()

print(student_one.created_at)
