def generate_squares(start, end):
    for x in range(start, end, 2):
        yield f'Square of {x} = {x ** 2}'


def generate_from(start, end):
    yield from generate_squares(start, end)


for square in generate_from(4, 16):
    print(square)
