class Person:
    GENDER_OPTIONS = ("female", "male")

    def __init__(self, gender, age, height, weight, name):
        self.__gender = self.__validate_gender(gender)
        self.age = age
        self.height = height
        self.weight = weight
        self.name = name

    def __validate_gender(self, gender):
        if gender not in self.GENDER_OPTIONS:
            raise ValueError(f"Gender value '{gender}' is not a valid one!")
        return gender

    def __new__(cls, *args, **kwargs):
        print("Creating person")
        return super().__new__(cls)

    def __str__(self):
        return f"I am {self.name}"

    def custom_method(self):
        print("Custom method from Person")

    @property
    def gender(self):
        return self.__gender

    @classmethod
    def create_person(cls, *args, **kwargs):
        # Do something
        return cls(*args, **kwargs)

    @staticmethod
    def some_static_method(*args, **kwargs):
        # Do something
        pass


# person_ani = Person("female", 23, 165, 55, "Ani")
# print(person_ani)


person_pesho = Person.create_person("male", 31, 180, 75, "Pesho")
print(person_pesho)
