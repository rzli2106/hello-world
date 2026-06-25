print("Starting debug practice...")
#print(name)
#NameError: a variable doesn't exist, typo or not defined

age = 19
#print("I am" + age + "years old") # TypeError: wrong data type, cannot concatenate string and int
#print("I am", age, "years old") or print(f"I am {age} years old") or print("I am" +str(age) + "years old")

fruits = ["apple", 13, "banana"]
#print(fruits[5]) # IndexError: index doesn't exist

student = {"name": "Richard", "age": 17, "favorite_fruit": "pineapple"}

#print(student["favorite_videogame"]) #keyError: key doesn't exist in dictionary

#use red dot on the left of numbers to set breakpoint, f5 for debug, f10 to step over, f11 to step into, shift+f11 to step out, f9 to continue
