is_true = True
is_false = False

amount_in_bank = 430
have_money = bool(amount_in_bank)
have_money_v2 = amount_in_bank > 0

print(have_money, have_money_v2)
# >>> True, True

print(bool([]))
# >>> False

print(bool(''))
# >>> False

print(bool({}))
# >>> False

print(bool(set()))
# >>> False

print(bool(0))
# >>> False

print(bool(1))
# >>> True

print(1 is None)
# >>> False
