student = {
    "name": "Richard",
    "age": 19,
    "courses": ["Math", "CS", "English"]
}

print(f"Student name: {student["name"]}") # older versions use single quotes for the string to avoid syntax errors

total_courses = len(student["courses"])
print(f"Total courses: {total_courses}")

for course in student["courses"]:
    print(course)

def show_age(age):
    if age == 18:
        print("Just turned adult!")
    else:
        print(f"Age is {age}")

show_age(student["age"])