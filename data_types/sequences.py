import string
from string import Template

print(string.ascii_letters)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)

name = "Pesho"
print(name[1::2])
print(8 * "x")

english_name = "John O'reilly"
multiline_string = """kjaslkdjalskd
jaslkdjalsda;sd
jalksjdalsdl;askd
kajslkdjalksjdlaksjd
kjaslkjdlaksjdlaksjd"""


name += str(31)

message = ["Header"]

for x in range(100):
    message.append(f"Message el {x}")

message_as_str = "\n".join(message)
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
sentence = "{name} is {aged} and lives in {living_place}."
print(sentence.format(name="Pesho", aged=28, living_place="Sofia"))
# >>> Pesho is 28 and lives in Sofia.

sentence_positional_example = "{0} is {1} and lives in {2}.".format("CodeAcademy", "8", "Sofia")
print(sentence_positional_example)

name = "CodeAcademyBG"
print("{:^100}".format(name))
print("{:<100}".format(name))
print("{:>100}".format(name))

print(name.startswith('N'))
print(name.endswith('M'))

name_as_array = list(name)
print(name_as_array)

name = ''.join(name_as_array)

print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))

code_academy = "CodeAcademyString"
print(code_academy[1:5])

template = Template("$who likes $what")
print(template.substitute(who=name, what="Programming languages"))

dict_args = dict(what="Football")

template_safe = Template("$who likes $what")
# print(template_safe.substitute(dict_args))
print(template_safe.safe_substitute(dict_args))

# define a simple ages list variable
ages_list = [14, 15, 14, 15, 16, 17, 8, 19, 18, 35]
ages_adults_list = [40 + x for x in range(10, 35, 5)]
name_as_list = list('CodeAcademy')
last_element = ages_list.pop()
is_twenty_in_ages_list = 22 in ages_list
print(is_twenty_in_ages_list)

print("Last element: {0}".format(last_element))
print("First element: {0}".format(ages_list[0]))

index_of_15 = ages_list.index(15)
print(index_of_15)

print("Length of ages_list: ", len(ages_list))

print("Count of 15 in ages_list ", ages_list.count(15))

# print("Index of 10001 in ages_list, ", ages_list.index(1001))

ages_list.sort(reverse=True)
print("Sorted version of ages_list: ", ages_list)

print("Sorted version of ages_adults_list: ", sorted(ages_adults_list, reverse=True))


# add new age to ages_list
ages_list.insert(20, 2)
ages_list.append(99)

# remove age from ages_list
ages_list.remove(14)

sliced_ages = ages_list[1:5]

# iterate over list
for age in ages_list:
    print(age)

for age in ages_list + ages_adults_list:
    print(age)


matrix_example = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

for matrix_el in matrix_example:
    print(matrix_el[-1], matrix_el[1])

for name, age, city in [("CodeAcademy", 8, "Sofia"), ("Name2", 12, "Sofia"), ("Name3", 15, "Sofia")]:
    matrix_example.append([name, age, city])

print(matrix_example)
matrix_example_as_comprehension = [[row[i] for row in matrix_example] for i in range(3)]
print(matrix_example_as_comprehension)

del matrix_example_as_comprehension[-1]

print("After deletion ", matrix_example_as_comprehension)


coords = (45.2545, 26.5874)
# coords += (487.212, 222.222)
print(coords)  # The result is new tuple coords created, not just mutated the original

print("Coord one ", coords[0])
print(len(coords))

x, y = coords
print(x, y)

for coord in coords:
    print(coord)
