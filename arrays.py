arr = ['jane', 'alice', 'charlie', 'dave', 'bob']
arr.sort() # sorts by alphabetical order
print(arr)

#custom sort
arr.sort(key=lambda x: len(x)) # sorts by length of string
print(arr)

arr = [i for i in range(5)]
print(arr)
arr = [i+i for i in range(5)]
print(arr)


arr = [0]*4
print(arr)
arr2d = [[0]*4 for i in range(3)] # creates a 2D array with 4 rows and 3 columns, all initialized to 0
arr2d[1][0] = 1 # second array, first column is 1
print(arr2d)
array = [[0 for i in range(4)] for j in range(3)] # creates a 2D array with 4 rows and 3 columns
print(array)