# define a simple dictionary where the key is the name and the value is the color of the fruit.
fruits_color = {
    'green_apple': 'green',
    'banana': 'yellow',
    'peach': 'orange',
}
print(fruits_color['green_apple'])
# >>> "green"


# Add new fruit
fruits_color['apricot'] = 'light_brown'

# remove element from dict
del fruits_color['banana']

# iterate over dict using .items()
for fruit, color in fruits_color.items():
    print(fruit, color)

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
        'age': '31',
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
        'age': '28',
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
