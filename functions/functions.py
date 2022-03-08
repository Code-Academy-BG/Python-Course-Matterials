def power(x, y):
    """ Returns x times y. """

    result = 1
    while y > 0:
        result *= x
        y -= 1
    return result


z = power(9, 2)
zz = power(x=9, y=2)
zzz = power(y=2, x=9)
# print(z)
# print(zz)
# print(zzz)


def power_v2(x, y=2):
    """ Returns x times y. """

    result = 1
    while y > 0:
        result *= x
        y -= 1
    return result


# print(power(2, y=3))
# print(power(y=3, x=2))
# print(power(y=3, 2))


#
def users_list(main_user, *users, main_user_age=None, main_user_city="Sofia", **users_options):
    print(main_user, main_user_age)
    for user in users:
        print(user, users_options[user])


# users_list(
#     'User1',
#     *[f'User{x}' for x in range(19)],
#     main_user_age=25,
#     **{f'User{x}': (x+1)*19 for x in range(19)},
# )


# Example of using mutable data types as function parameters
def update_ages(age, passed, future):
    passed.append(age)
    age += 1
    future = [age + x for x in range(1, 4)]
    print(age, future)


mine_age = 31
passed_ages = [_ for _ in range(1, mine_age)]
next_three_ages = [mine_age + _ for _ in range(1, 4)]

update_ages(mine_age, passed_ages, next_three_ages)
print('After update_ages executed')
print(mine_age, passed_ages, next_three_ages)


age_module_scope = 31
print('Module scope: ', age_module_scope)


# Scope test
age_module_scope = 31


def scope_test():
    var_one = 5
    var_two = 6
    ages = [25]

    def scope_inner_test():
        global age_module_scope
        age_module_scope += 5
        var_one = 6
        var_two = 7
        ages.append(26)
        print('Inner scope: ', var_one, var_two, ages, age_module_scope)

    scope_inner_test()
    print('Outer scope: ', var_one, var_two, ages, age_module_scope)


# scope_test()

# function assigned as a value of a variable
def add_two(x):
    x += 2
    return x


variable_add = add_two

# print(variable_add(5))

# Not recommended
variable_add = lambda x: x + 2
# print(variable_add(5))


students_data = [
    {
        'name': 'Tosho',
        'age': 25,
        'discipline': 'mathematics',
    },
    {
        'name': 'Gosho',
        'age': 27,
        'discipline': 'IT',
    },
    {
        'name': 'Ivan',
        'age': 29,
        'discipline': 'informatics',
    }
]

students_data.sort(key=lambda data: data['discipline'])
# print(students_data)


def mutate_list(name: str, names=[]):
    names.append(name)
    return names


def func1():
    x = 5


def func2():
    global x
    x = 9

# func1()
# func2()
# print(x)


def divide_by_five(x):
    return x / 5


test_dict = {"add_two": add_two, "divide_by_5": divide_by_five}
print("From dict call: ", test_dict["add_two"](5))
print("From dict call: ", test_dict["divide_by_5"](30))

"""
password_checker = [
    check_length,
    check_random,
    check_strength,
    ....
]

password = "random password"

for check password_checker:
    if not check(password):
        print("Invalid password")
        break
"""
