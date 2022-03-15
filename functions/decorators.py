from contextlib import contextmanager
from functools import wraps, singledispatch


def pre_tag(func):
    @wraps(func)
    def wrapper_func(*args):
        func_result = func(*args)
        return f'<pre>{func_result}</pre>'
    return wrapper_func


def bold(func):
    @wraps(func)
    def wrapper_func(*args):
        func_result = func(*args)
        return f'<b>{func_result}</b>'
    return wrapper_func


@pre_tag
@bold
def print_name(name):
    """print_name decorated function docstring"""
    return name


help(print_name)


"""
Checkout what print_name.__doc__ before and after applying @wraps(func) on the decorator 
functions.

The same is valid for decorated_print_name as well.
"""

# print_name('Pesho')
# decorated_print_name = pre_tag(bold(print_name))


def encode_id(func):
    @wraps(func)
    def wrapper_func(user_id):
        return f'encoded_{func(user_id) * 1200}_user_id'
    return wrapper_func


@encode_id
def get_user_id(user_id):
    return user_id


print(get_user_id(143))


@singledispatch
def printer(value):
    print(f"Other: {value}")


@printer.register(str)
def str_printer(value):
    print("Print string: ", value)


@printer.register(int)
def int_printer(value):
    print("Print integer: ", value)


@printer.register(dict)
def dict_printer(dictionary):
    for value in dictionary.values():
        print("Value of dict item is: ", value)


printer({"name": "C", "name2": "Python"})


@contextmanager
def debug(name):
    print("Debugging: ", name)
    yield
    print("End of debugging ", name)


@debug("print_function")
def print_function(some_text):
    print(f"This is inside of our print_function, with arg: {some_text}")


print_function("Function, Generators and Decorators lecture, pt. 3")
