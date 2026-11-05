# We import json because we need python to understand what is written in json. Also, we will be using it in the future for AI implementation and it is used to save the file in the computer.
import json

# os is used to check if the file exists and its size
import os

# For convenience, we save the name of the file into a variable so that if we wanted to change the file name, we don't need to be searching every line in the future in the code. This way it is way more convenient.
fileName = "fileName2.json"

# I have created different functions for clarity:


# This function will save the dictionary and it will be called when needed for so
def save_diccion(diccion):
    with open(fileName, "w", encoding="utf-8") as archive:
        json.dump(diccion, archive, indent=4)


# This one will simply load the dictionary
def load_diccion():

    # We check first if the file exists and we also check if the size of it does as well
    if not os.path.exists(fileName) or os.path.getsize(fileName) == 0:
        # This print will indicate us in the console when it does not
        print("The file does not exist or is empty. Creating default contacts...")
        diccion = {"Pablo": 654345234, "Rodrigo": 7574737234, "David": 984528234}
        # We call the function save to save the dictionary to json
        save_diccion(diccion)
        return diccion

    # This will be used if the file is already existing
    with open(fileName, "r", encoding="utf-8") as archive:
        return json.load(archive)


# This is the function that will print the dictionary
def show_diccion(diccion):
    # In order for the print to be aesthetically pleasing, we use the ind (index) to numerate each name. Also, enumerate is used when we want to access the index as well apart from the collection. Start 1 is used because Python numbering always starts at 0, so we commanded it to be from 1.
    for ind, (name, phoneNum) in enumerate(diccion.items(), start=1):
        print(f"{ind}. {name} -> {phoneNum}")


# We need to call the function in order for it to be executed
diccion = load_diccion()


# Here I used the example of, what if we wanted to add a contact later on? For example Andres:

# We update the dictionary in Python first
diccion.update({"Andres": 655987878})
save_diccion(diccion)

# We show the end result of the dictionary
show_diccion(diccion)
