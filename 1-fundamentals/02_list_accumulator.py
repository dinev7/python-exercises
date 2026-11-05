# We create a list of numbers
numbers = [12.5, 40.0, 5.25, 99.99]
# We create a counter that will be adding on to the total value
counter = 0

# We go through each number of the list and we added it to our total counter
for num in numbers:
    counter = num + counter
    # We want to know if the specific item exceeds 50, then it means that it is too expensive.
    if num > 50:
        print("Expensive item found!")


# We print the total ammount
print("The total price of the items are: ", counter)
