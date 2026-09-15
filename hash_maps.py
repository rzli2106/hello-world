#Hashmaps/Dicitonaries - key and definition
myMap = {}
myMap["Richard"] = 88
myMap["John"] = 66

print(myMap)
print(len(myMap)) # gives number of keys that exist

myMap["Richard"] = 77 # can't have duplicate keys
print(myMap["Richard"])

print("Richard" in myMap) # search if key is in hashmap
myMap.pop("Richard") 
print("Richard" in myMap)

myMap = {"Richard" : 100, "John": 60} 
print(myMap)

myMap2 = {i : i * 2 for i in range(5)} #{i is the key : i * 2 is the definition}
print(myMap2)

#looping through hashmaps
for key in myMap2:
    print(key, myMap2[key]) # print key and definition

#alternative version
for key, val in myMap2.items():
    print(key, val)

for val in myMap2.values(): # only need values
    print(val)