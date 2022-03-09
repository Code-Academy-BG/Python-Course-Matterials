from functools import wraps


def pre_tag(func):
    # @wraps(func)
    def wrapper_func(*args):
        func_result = func(*args)
        return f'<pre>{func_result}</pre>'
    return wrapper_func


def bold(func):
    # @wraps(func)
    def wrapper_func(*args):
        func_result = func(*args)
        return f'<b>{func_result}</b>'
    return wrapper_func


@pre_tag
@bold
def print_name(name):
    """print_name decorated function docstring"""
    return name


"""
Checkout what print_name.__doc__ before and after applying @wraps(func) on the decorator 
functions.

The same is valid for decorated_print_name as well.
"""

# print_name('Pesho')
decorated_print_name = pre_tag(bold(print_name))


def encode_id(func):
    @wraps(func)
    def wrapper_func(user_id):
        return f'encoded_{func(user_id) * 1200}_user_id'
    return wrapper_func


@encode_id
def get_user_id(user_id):
    return user_id


print(get_user_id(143))
