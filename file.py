#with open("notes.txt", "w") as file: w deletes everything and writes
#    file.write("My first saved line!\n")
'''
note = input("Write your note:")

with open("notes.txt", "a") as file: # a appends to file instead of writing over it
    file.write(note + "\n")

with open("notes.txt", "r") as file: # r reads the file
    content = file.read()
    print("Current file:")
    print(content)
'''

name = input("What is your name?")
fact = input("What is a fun fact about you?")

with open("about_me.txt", "a") as file:
    file.write(name + "\n")
    file.write(fact + "\n")

with open("about_me.txt", "r") as file:
    content = file.read()
    print(content)