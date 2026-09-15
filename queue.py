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