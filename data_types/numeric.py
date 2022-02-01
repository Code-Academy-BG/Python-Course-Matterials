"""
Within this module you'll find numerical data types that we'll be talking about. You can find
and use the examples the way you like.
"""

from decimal import Decimal


bags_count = 15  # integer
print(bags_count)
# >>> 15

shirts_count = 10
print(shirts_count)
# >>> 20

# Operations that can be done with integers
"""
    bags_count + shirts_count = 25 # Sum
    bags_count += 2 # Short version of bags_count = bags_count + 2 (Output: 17)
    
    bags_count - shirts_count = 5 # Difference
    bags_count -= 2 # Short version of bags_count = bags_count - 2 (Output: 13)

    bags_count * shirts_count = 150 # Product
    bags_count *= 2 # Short version of bags_count = bags_count * 2 (Output: 30)
    
    bags_count / shirts_count = 1.5 # quotient
    bags_count /= 2 # Short version of bags_count = bags_count / 2 (Output: 7.5)
    
    bags_count // shirts_count = 1 # floored quotient
    bags_count //= 2 # Short version of bags_count = bags_count // 2 (Output: 7)
    
    bags_count % shirts_count = 5 # reminder
    bags_count %= 2 # Short version of bags_count = bags_count % 2 (Output: 2)
    
    abs(b) --- absolute value of b
    abs(15)
    >>>15
    abs(-15)
    >>>15
    
    pow(bags_count, power) ---> bags_count ** power
    
    Sames operators are applicable to Float as well.
"""

base_coef = 4.5  # float
coef_multiplier = 2
print(base_coef * coef_multiplier)
# >>> 9.0

print(base_coef * coef_multiplier == 9.0)  # Expect True?
# >>> True it is

print(base_coef * 3 == 13.5)  # Expect True?
# >>> Nope, False it is, due to the floating point unit *** Check this out

shipping_price = Decimal('6.5')  # Decimal
print(shipping_price)
print(shipping_price * 3 == Decimal('19.5'))  # Expect True?
# >>> True it is
