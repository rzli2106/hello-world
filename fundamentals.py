student = {
    "name": "Richard",
    "age": 17,
    "favorite_fruit": "pineapple"
}
print(f"Hello my name is {student["name"]} and I am {student["age"]} year old. My favorite fruit is {student["favorite_fruit"]}")

favorite_things = ["pineapple", "fortnite", "coding", "dogs"]
for thing in favorite_things:
    print(f"I like {thing}")

def is_adult(age):
    if age >= 18:
        print("You are an adult")
    else:
        print("You are not an adult")

is_adult(17)