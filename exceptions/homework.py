import os

import requests

from settings.testing import INPUT_DIR

try:
    5 / 0
except ZeroDivisionError:
    print("Not a good practice to delete by 0")

try:
    Decimal("100")
except NameError:
    print("Hm, it seems, there is no such module in my scope?")

try:
    open(os.path.join(INPUT_DIR, "some_nasty_bug_file.txt"))
except FileNotFoundError:
    print("You're trying to cheat me with some buggy file, don't you!")

try:
    list_a = range(29)
    list_a[5]
except IndexError:
    print("Please learn the range API before attempt to use it.")

try:
    dict_b = {"some_key": "some_value", 5: 10, (): False}
    dict_b[True]
except KeyError:
    print("I don't have True value")

try:
    list_a.pesho
    dict_b.codeacademy
except AttributeError:
    print("What are you trying to achieve?")

try:
    print(AmIRealObject)
except NameError:
    print("AmiRealObject is not a real object, or at least I don't have it inside my scope")

try:
    response = requests.post("http://alabala.koisiti")
except requests.ConnectionError:
    print("alabala.koisiti is not available for you")
