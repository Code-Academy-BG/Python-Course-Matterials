def pre_tag(func):
    def wrapper_func(*args):
        print(f'<pre>{func(*args)}</pre>')
    return wrapper_func


@pre_tag
def print_name(name):
    return name


print_name('Pesho')


def encode_id(func):
    def wrapper_func(user_id):
        return f'encoded_{func(user_id)}_user_id'
    return wrapper_func


@encode_id
def get_user_id(user_id):
    return user_id


print(get_user_id(143))
