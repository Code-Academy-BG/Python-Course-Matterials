def generate_100():
    for x in range(1, 101):
        yield x
        yield x + 1


for x in generate_100():
    print(x)
