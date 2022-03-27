#!/usr/bin/env python3

# Python 3.9.5

# deque.py

# Purpose: deque - double-ended queue

# Dependency:
import collections

data = collections.deque([4, 9, 17])
print('New created:', data)
data_copy = data.copy()
print('Copy of data:', data_copy)

print("Printing out all elements: ", end="\n")
for d in data:
    print(data, end = "\n ")

# Single elements
try:
    print('Second element from the left:', data[1])
except:
    print("This index doesn't exist")

try:
    print("First element from the right:", data[-1])
except:
    print("This index doesn't exist")

# Multiply
data = data * 2

# Add
data = data + data_copy

# Clear deque
data.clear()
