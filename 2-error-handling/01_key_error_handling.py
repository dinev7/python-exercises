# We create specifically an empty dictionary
diccion = {}
# We add attributes to the dictionary with the key: being the name and their phone number being the value:
diccion.update({"Pablo": 654345234, "Rodrigo": 7574737234, "David": 984528234})
# We print the dictionary showing that we successfully created it
print(diccion)

# We use try and except to find the specific number from Pablo. If there was a case when we wouldn't find it, instead of the program showing us an error, it will print in the console what we indicate it to and we by-pass the error.
try:
    print(diccion["Pablo"])
except KeyError:
    print("The name you're looking for was not found")


# We create a function that will find the specific key, in this case the name, from the value, aka the phone number
def findKey(value):
    key_found = None
    # We go through the dictionary. K is used for key, V is used for value and we use .items because it returns us both the key and the value
    for k, v in diccion.items():
        # When the variable value is the same as the real value, then we associate the key with the variable key_found
        if v == value:
            key_found = k
            break
    # And here we print the key, in this case, the name.
    print(key_found)


# Here we send the number we want to find to the function, and it prints the name that belongs to it
findKey(7574737234)
