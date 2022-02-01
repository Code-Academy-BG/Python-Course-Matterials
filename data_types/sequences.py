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
ages_list = [14, 15, 14, 15, 16, 17, 8, 19, 18]
