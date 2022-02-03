if True:
    print('Me')


if True:
 # This one would raise an Indentation error, because line 7 indentation is different from line 6's
 print('Me')
  # print('Me')


age = 18
age_min = 25

if age < age_min:
    print('Your age is not allowed for this operation')
elif age == age_min:
    print('Hm, you pass the age condition, but you have still a lot to grow ;) ')
else:
    print('You are very welcome')


age = 27
if age < age_min:
    print('Your age is not allowed for this operation')
elif age == age_min:
    print('Hm, you pass the age condition, but you have still a lot to grow ;) ')
print("I'm just a happy output")


# Nesting ifs
if True:
    if True:
        if True:
            pass
        else:
            pass
    else:
        pass
else:
    pass
