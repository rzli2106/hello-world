'''n = 0
print(n)
n = 'abc'
print(n)

x, y = 1, 2
n += 1
n = None
print(n)'''

#n = 0
#while n < 10:
#    print(n)
#    n += 1
import math
#math.fmod gives remainder
#math.floor rounds down
#math.ceil rounds up
#math.sqrt gives square root

'''float("inf")
float("-inf")

for i in range(2,5):
    print(i)

    

#lists/arrays
list = [1, 2, 3, 4, 5]
list.append(6)
list.append(7)
list.pop()
print(list)

list.insert(1,7) #inserting 7 at index 1
list[0] = 10 #changing value at index 0 to 10
print(list)
print(len(list)) #length of list
print(list[0:3]) #slicing list from index 0 to 2'''



#array for loops
'''nums = [1, 2, 3, 4, 5]
for i in range(len(nums)):
    print(nums[i])

for n in nums:
    print(n)

#index and value
for i,n in enumerate(nums):
    print(i, n)'''

'''
#multiple arrays
nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 10]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)

#reversing an array
nums2.reverse()
print(nums2)

#sorting an array
nums3 = [2, 50, 4, 9, 1, 3]
nums3.sort()
print(nums3)
nums3.sort(reverse=True)
print(nums3)
'''

'''arr = ['jane', 'alice', 'charlie', 'dave', 'bob']
arr.sort() # sorts by alphabetical order
print(arr)

#custom sort
arr.sort(key=lambda x: len(x)) # sorts by length of string
print(arr)

arr = [i for i in range(5)]
print(arr)
arr = [i+i for i in range(5)]
print(arr)'''

"""
#arr = [0]*4
#print(arr)
arr2d = [[0]*4 for i in range(3)] # creates a 2D array with 4 rows and 3 columns, all initialized to 0
arr2d[1][0] = 1 # second array, first column is 1
print(arr2d)
array = [[0 for i in range(4)] for j in range(3)] # creates a 2D array with 4 rows and 3 columns
print(array)"""

string = 'abc'
print(int("123") + int("456")) # can convert to and from int
print(str(123) + str(456)) #adding strings together appends them

strings = ["abc", "def", "ghi"]
print(" ".join(strings)) # joins strings together

from collections import deque
#deque is a double ended queue, can add and remove from both ends
d = deque()
d.append(0)
d.append(2)
print(d)

d.popleft()
print(d)

d.appendleft(0)
print(d)

