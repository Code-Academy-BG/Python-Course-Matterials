name = 'Pesho'
print(name[1::2])
print(8 * "x")

english_name = 'John O\'reilly'
multiline_string = """kjaslkdjalskd
jaslkdjalsda;sd
jalksjdalsdl;askd
kajslkdjalksjdlaksjd
kjaslkjdlaksjdlaksjd"""


name += str(31)

message = ['Header']

for x in range(100):
    message.append(f'Message el {x}')

message_as_str = '\n'.join(message)
# print(message_as_str)


# print(name)  # Hm, this is possible, but string is immutable?
# print(name.title())
# print(name.capitalize())
# print(name.isalnum())
# print(name.isalpha())
# print(name.isdigit())
# print(name.zfill(5))
# print(message_as_str.split())


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

