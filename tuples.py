# similar to arrays but cant be changed
tup = (1, 2, 3)
print(tup)
print(tup[0])


# can't modify
#tup[0] = 0 wont work

#used for keys in hashmaps and hashsets bc lists cant be used

myMap = {(1,2): 3}
print(myMap[(1,2)])

mySet = set()
mySet.add((1,2))
print((1,2) in mySet)
