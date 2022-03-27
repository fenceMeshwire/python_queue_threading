#!/usr/bin/env python3

# Python 3.9.7

# fifo_queue.py

# Purpose: FIFO queue - first element in first element out

# Dependency:
import queue

data = queue.SimpleQueue()
print('Number of elements:', data.qsize())

data.put(7) # Adding elements with .put()
data.put(21)
data.put(-5)
data.put(4)

print('Number of elements:', data.qsize())

while not data.empty():
    print(data.get()) # Removing elements with .get()
print('Number of elements:', data.qsize())
