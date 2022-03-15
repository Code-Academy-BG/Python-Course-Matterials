import random
from datetime import date
from functools import wraps


# For the next functions, it is up to you to determine the names they should have
# 3. Write a function that would return if given int is within a certain range
# 4. Write a Python function to create and print a list where the values are square of numbers
# between 1 and 30 (both included)
# **5. Write a function that accepts multidimensional list and prints out list elements nested by
# their dimension:
# Example: [[1, 2, [3, 4, [6]]], [[], [], [3, 4, 5]]]
# 1, 2
#      3, 4
#      6
#
#
#      3, 4, 5
#
# Hint: You may, or you may not use recursion


# Decorators
# 1. Write a decorator that would be used on a function that return a number. If today is wednesday,
# friday, or sunday, the function should return the number decreased byt 1.5.
# 2. Write decorator login_required that would be used to check if a user is logged, and if not,
# it should print out "Login required", and if user is logged, the decorated function should print
# "Welcome"
# For user you can use {'name': 'User name', 'logged': True / False}
# 3. Write a decorator that prints out "Mary Spring" whenever the decorated function is called.


def get_min_of_three_members(x, y, z):
    def _min_of_two_numbers(a, b):
        return a if a < b else b

    return _min_of_two_numbers(x, _min_of_two_numbers(y, z))


print(get_min_of_three_members(5, 89, 2))


def reverse_string(string):
    return "".join([string[i] for i in range(len(string) - 1, -1, -1)])


print(reverse_string("CodeAcademy helps motivated men to become techs."))


def get_is_number_in_range(x, start, end):
    return x in range(start, end + 1)


print(get_is_number_in_range(8, 4, 20))


def get_squares():
    squares = [str(x**2) for x in range(1, 31)]
    print(", ".join(squares))


get_squares()


def print_matrix(matrix, indent=0):
    for el in matrix:
        if isinstance(el, list):
            print()
            print_matrix(el, indent + 4)
        else:
            print(" " * indent, el, end="")
            indent = max(indent - 4, 4)
    print()


print_matrix([
    [1, 2, [3, 4, [6]]],
    [[], [], [3, 4, 5]],
])


def decrement_base_on_day(func):
    @wraps(func)
    def wrapped_func(*args):
        func_result = func(*args)
        today = date.today()
        if today.weekday() in [2, 4, 6]:
            print(
                f"As today is {today.strftime('%A')}, you get discount of 1.5"
                f" of your bill {func_result}"
            )
            return func_result - 1.5
        return func_result
    return wrapped_func


@decrement_base_on_day
def get_number(n):
    return n


print(get_number(25))


def login_required(func):
    @wraps(func)
    def wrapped_func(user, *args, **kwargs):
        if user["logged"]:
            print(f"Welcome {user['name']}")
            return func(user, *args, **kwargs)
        else:
            print("Login required")

    return wrapped_func


@login_required
def check_emails(user):
    print(f"Checking user {user['name']} emails")


check_emails({"name": "User name", "logged": True})


def marry_spring(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        print("Marry spring")
        return func(*args, **kwargs)

    return wrapper_func


@marry_spring
def some_function():
    print("I'm just a function defined in Spring!")


some_function()
