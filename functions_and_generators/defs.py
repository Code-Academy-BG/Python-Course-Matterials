def power(x, y):
    """ Returns x times y. """

    result = 1
    while y > 0:
        result *= x
        y -= 1
    return result


print(power(2, 3))


def power_v2(x, y=2):
    """ Returns x times y. """

    result = 1
    while y > 0:
        result *= x
        y -= 1
    return result


print(power(2, y=3))
print(power(y=3, x=2))
# print(power(y=3, 2))


def users_list(main_user, *users, main_user_age=None, **users_options):
    print(main_user, main_user_age)
    for user in users:
        print(user, users_options.get(user))


users_list(
    'User1',
    *[f'User{x}' for x in range(19)],
    main_user_age=25,
    **{f'User{x}': (x+1)*19 for x in range(19)},
)
