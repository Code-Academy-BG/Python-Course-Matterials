# Example:
# while <condition>:
#     do something
#     <do something to update condition>

counter = 0
while counter < 5:
    print(f'Counter value is: {counter}')
    counter += 1  # If we don’t add this line, we’ll simply enter an infinite loop
