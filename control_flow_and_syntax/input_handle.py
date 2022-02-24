# from control_flow_and_syntax.cycle_import import Test


def get_user_age():
    user_age = input('Please enter your age: ')
    print(type(int(user_age)) == int)
    print(int(user_age))


def get_user_details():
    user_details = input('Please enter your name and age: ')
    print(', '.join(user_details.split(' ')))


get_user_age()
