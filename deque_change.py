#!/usr/bin/env python3

# Python 3.9.5

# deque_change.py

# Purpose: Change values in the double ended queue.

# Dependency:
import collections

data = collections.deque([4, 9, 23])

# Append single values to deque
data.appendleft(5)
data.append(25)
data # check result

# Insert value 11 on position 2
data.insert(2, 11)
data # check result

# Extend by several elements
data.extendleft([7, 9])
data.extend([7, 9])
data # check result

# Find element within deque
try:
    print('Position of the 3rd value:', data.index(3))
except:
    print('Value not available.')

# Remove single elements left within a for loop
for i in range(len(data) - 2):
    left = data.popleft()

# Remove single elements right
right = data.pop()
right # check result

# Rotate queue internally
data = collections.deque([4, 9, 23])
data.rotate()
data # check result
data.rotate(-1)
data # check result
