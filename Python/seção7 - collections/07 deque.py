from collections import deque

deq1 = deque('name')
deq2 = deque()
print(deq1)
print(deq2)

deq1.append(' ')
deq1.append('w')
deq1.appendleft('W')
print(deq1)
last = deq1.pop()
first = deq1.popleft()
print(first)
print(last)
