# define a simple dictionary where the key is the name and the value is the color of the fruit.
from collections import OrderedDict, defaultdict, Counter
import random

fruits_color = {
    'green_apple': 'green',
    'banana': 'yellow',
    'peach': 'orange',
}

ordered_dict = OrderedDict([
    (1, 'Pesho'),
    (2, 'Gosho'),
    (3, 'Ivan'),
])


has_key = hash('green_apple')
print(has_key)
print(fruits_color['green_apple'])
print(fruits_color.get('pesho'))
# >>> "green"

has_banana = 'banana' in fruits_color
print(has_banana)

fruits = len(fruits_color)

# Add new fruit
fruits_color['apricot'] = 'light_brown'
fruits_color['green_apple'] = 'brown'
print(fruits_color)

# remove element from dict
del fruits_color['banana']

# iterate over dict using .items()
for fruit, color in fruits_color.items():
    print(fruit, color)

for fruit in fruits_color:
    print(fruit, fruits_color[fruit])

for fruit_color in fruits_color.values():
    print(fruit_color)

# 'green_apple', 'green'
# 'peach', 'orange'
# 'apricot', 'light_brown'

# iterate over the .keys()
for fruit in fruits_color:
    print(fruit, fruits_color[fruit])

# 'green_apple', 'green'
# 'peach', 'orange'
# 'apricot', 'light_brown'

for fruit in fruits_color.keys():
    print(fruit, fruits_color[fruit])

# 'green_apple', 'green'
# 'peach', 'orange'
# 'apricot', 'light_brown'

# iterate over the .values()
for fruit_color in fruits_color.values():
    print(fruit_color)

# 'green'
# 'orange'
# 'light_brown'


# dictionary with nested data
students_data = {
    'student_1': {
        'name': 'Pesho',
        'age': 31,
        'courses': [
            {
                'title': 'SQL',
                'period': '2022-01-01 - 2022-03-01',
                'credits': 10,
            },
            {
                'title': 'C',
                'period': '2021-12-01 - 2022-03-01',
                'credits': 20,
            },
            {
                'title': 'Python',
                'period': '2022-02-22 - 2022-04-22',
                'credits': 15,
            },
        ],
    },
    'student_2': {
        'name': 'Gosho',
        'age': 28,
        'courses': [
            {
                'title': 'SQL',
                'period': '2022-01-01 - 2022-03-01',
                'credits': 10,
            },
            {
                'title': 'C',
                'period': '2021-12-01 - 2022-03-01',
                'credits': 20,
            },
            {
                'title': 'Python',
                'period': '2022-02-22 - 2022-04-22',
                'credits': 15,
            },
        ],
    },
}

for student, student_data in students_data.items():
    print(student_data['name'], student_data['age'])
    # continue with iteration of the 'courses'

    print('Courses:')
    for course in student_data['courses']:
        # a little shortcut if we only want to print the values
        print(*course.values())


dict_comprehension = {}
for x in range(1, 5):
    # if condition:
    #   pass
    dict_comprehension[x**4] = random.choice('asdsadasdasdasdaasdasd')

# dict_comprehension = {
#     x**4: random.choice('asdsadasdasdasdaasdasd')
#     for x in range(1, 5)
# }

for key, value in dict_comprehension.items():
    print(f"Key: {key}\n     Value: {value}".format(
        key=key,
        value=value,
    ))

students_info = [
    {
        "name": "Pesho",
        "points": 15,
    },
    {
        "name": "Ivan",
        "points": 20,
    },
    {
        "name": "Tisho",
        "points": 45,
    },
    {
        "name": "Pesho",
        "points": 7,
    },
]

students_info_dict = {}
for info in students_info:
    students_info_dict.setdefault(info['name'], 0)
    students_info_dict[info['name']] += info['points']

for student_name, student_points in students_info_dict.items():
    print(student_name, student_points)


default_dict_example = defaultdict(list)
for name in ['Gosho', 'Tisho', 'Ivan']:
    default_dict_example[name].append(random.random())

print(default_dict_example)

default_dict_example_two = defaultdict(lambda: {'old_data': {}, 'new_data': {}})
default_dict_example_two['Python']['old_data']['date'] = '2022-02-22'

print(default_dict_example_two)


counter_example = Counter('CodeAcademyBG')
print(counter_example)


students_info_tuples = {
    ("CodeAcademy", 8): "Sofia",
    ("Name", 25): "Sofia",
    ("Name2", 17): "Sofia",
    ("Name3", 36): "Sofia",
}

for (name, age), city in students_info_tuples.items():
    print(name, age, city)
