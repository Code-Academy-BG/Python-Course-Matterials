fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruits)

# In other words:
# for var in iterable:
#     do something


for fruit in fruits:
    if len(fruit) < 3:
        continue
    elif len(fruit) > 100000:
        continue
    else:
        print(fruit)
        # break This would cause an immediate exit from the loop
