#!/usr/bin/env python3

# Python 3.9.7

# priority_queue.py

# Purpose: priority queue - sorts the elements in an ascending order

# Dependency:
import queue

data = queue.PriorityQueue()
data.put(7) # Adding elements with .put()
data.put(21)
data.put(-5)
data.put(4)
while not data.empty():
    print(data.get()) # Retreiving elements with .get()
