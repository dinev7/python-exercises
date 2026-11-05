# We create a list with several different numbers
numbers = [4, -3, 0, 15, -8, 22]


# We create a function where we print the text, this will save us later writting extra repetitive code in the for
def showString(String):

    print(String)


# Now we go through every number on the list in a linear way through a for
for i in numbers:
    # We check if the number is positive, negative, or zero
    if i > 0:
        showString(f"The number {i}, is positive")
    elif i < 0:
        print(f"The number {i}, is negative")
    else:
        print(f"The number {i} is 0")

    # In order to know if it's even, when we divide the number to 2, the rest must be 0
    if i % 2 == 0:
        print(f"The number {i}, is even")

    else:
        print(f"The number {i}, is odd")
