import random
from itertools import tee


class Repeater:
    def __init__(self, value):
        self.value = value
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < 10:
            self.start += 1
            return self.value
        raise StopIteration("Endless iterator is dangerous")


repeater = Repeater("hello")

for x in repeater:
    print(x)


class FirstN:
    def __init__(self, n):
        self.n = n
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < self.n:
            current, self.num = self.num, self.num + 1
            return current
        raise StopIteration()


print(sum(FirstN(505)))


def first_n(n):
    num = 0
    while num < n:
        yield num
        num += 1


def endless_generator():
    while True:
        yield "CodeAcademy"


def generate_squares(start, end):
    for x in range(start, end, 2):
        yield x
        # yield f'Square of {x} = {x ** 2}'


def generate_from(start, end):
    yield from generate_squares(start, end)


def generate_negate(seq):
    for el in seq:
        yield -el


# A little example of chaining generators
for negate_square in generate_negate(generate_squares(4, 22)):
    print(negate_square)

# for square in generate_from(4, 16):
#     print(square)


def chars():
    for x in range(1, 9):
        yield f"p{x}"


def chars_multiplied(seq):
    for c in seq:
        yield c * 2


def chars_reversed(seq):
    for c in seq:
        yield c[::-1]


for c in chars_reversed(chars_multiplied(chars())):
    print(c)


def generate_students_info():
    for e in range(1, 11):
        for s in range(1, 281):
            yield f"Student {s}", {
                "student_name": f"Student {s}",
                "exam": e,
                "points": random.randint(random.choice([30, 40, 50]), 100),
            }


a, b = tee(range(24))

for x in a:
    print(x)

for y in b:
    print(y)
