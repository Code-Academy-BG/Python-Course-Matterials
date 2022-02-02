name = 'Pesho'

name += str(31)

print(name)  # Hm, this is possible, but string is immutable?
print(name.title())
print(name.capitalize())
print(name.isalnum())
print(name.isalpha())
print(name.isdigit())
print(name.zfill(5))
print(name.split())


# formatted string
sentence = '{name} is {aged} and lives in {living_place}.'
print(sentence.format(name='Pesho', aged=28, living_place='Sofia'))
# >>> Pesho is 28 and lives in Sofia.


# define a simple ages list variable
ages_list = [14, 15, 14, 15, 16, 17, 8, 19, 18, 35]

# add new age to ages_list

# remove age from ages_list
ages_list.remove(14)

# iterate over list
for age in ages_list:
    print(age)


coords = (45.2545, 26.5874)
coords += (487.212, 222.222)
print(coords)  # The result is new tuple coords created, not just mutated the original

for coord in coords:
    print(coord)

