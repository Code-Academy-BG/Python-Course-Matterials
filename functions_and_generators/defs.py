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


scope_test()
