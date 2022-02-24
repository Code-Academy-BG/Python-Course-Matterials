# Example:
# while <condition>:
#     do something
#     <do something to update condition>

counter = 0
while counter < 5:
    # if condition:
    #   do something
    print(f'Counter value is: {counter}')
    counter += 1  # If we don’t add this line, we’ll simply enter an infinite loop
else:
    print("CodeAcademy")


counter = 0
while True:
    print("Counter", counter)
    counter += 1
    if counter > 100:
        break
