import random

from datetime import datetime


class MyError(Exception):
    pass


try:
    raise MyError("Message 1 raised at: ", datetime.now())
except MyError as err:
    print(f"Error occured: {err.args[0]} at {err.args[1]}")


some_exceptions = [ValueError, TypeError, IndexError, None]

try:
    choice = random.choice(some_exceptions)
    print("raising {}".format(choice))
    if choice:
        raise choice("An error")
except ValueError:
    print("Caught a ValueError")
except TypeError:
    print("Caught a TypeError")
except Exception as b:
    print("Caught some other error: %s" % b.__class__.__name__)
else:
    print("This code called if there is no exception")
finally:
    print("This cleanup code is always called")


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def is_legit_for_disco(self):
        return self.age >= 18

    def enter_disco(self):
        print(f"User {self.name} tries to enter the disco")
        assert self.is_legit_for_disco
        print("Welcome to the disco")


names = ["Pesho", "Gosho", "Toni"]
ages = [14, 20, 18]

for user_data in zip(names, ages):
    user = User(*user_data)
    try:
        user.enter_disco()
    except AssertionError:
        print(f"{user.name}, you're not allowed to enter the disco")


def get_element_of_list(element):
    assert isinstance(element, int)

    temp_list = list(range(1, 19))
    return temp_list[element]


def test_bad_exit():
    print("Bad exit?")
    exit(2)
