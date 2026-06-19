name = "Richard" #string
age = 17 #integer
height = 5.7 #float
is_student = True #boolean

print(type(name)) # prints what type of data

first = "Richard"
last = "Li"

full_name = first + " " + last # adding two strings
print(full_name)

print(f"My name is {full_name} and I am {age} years old.") # f-string to embed variables in a string

if age >= 21: # if statement 
    print("You can drink")
elif age >=18: # else if 
    print("You are an adult but cannot drink") # else
else:
    print("You are a minor")

# for if statments: == is equal to, != is not equal to, 
# > greater than, < less than, >= greater than or equal to, <= less than or equal to

fruits = ["apple", "banana", 19] # list can contain different data types
for x in fruits: # x is a temporary variable and can be named anything, it will take on the value of each item in the list as it loops through
    print(x) 

for i in range(5): # range generates a sequence of numbers, in this case from 0 to 4
    print(i)

countdown = 3
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Blast off!")


def greet(user_input): # name is a parameter
    print(f"Hello, {user_input}!")

greet("Richard")
greet(190)
greet(1.03) # functions can take any data type as an argument

def add(a, b):
    return a + b

result = add(3, 10)
print(result)
test = add("Hello, ", "world!")
print(test)

grades = [25, 93, 100, 95, 88]
print(grades[0]) # start at 0 so 25
print(grades[-1]) # negative starts from end so 88
print(grades[1:4]) # index 1 to 3, 4 not included
print(len(grades)) # length of list
print(sum(grades)) # sum of grades
average = sum(grades) / len(grades)
print(average)

grades.append(94) # adds 94 to end
grades.remove(25) # removes 25
print(grades)
grades.sort() # sorts in ascending order 
print(grades)