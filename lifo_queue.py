#!/usr/bin/env python3

# Python 3.9.7

# 02_lifo_queue.py

# Purpose: LIFO queue - last element in first element out

# Dependency:
import queue

data = queue.LifoQueue()
data.put(7) # Adding elements with .put()
data.put(21)
data.put(-5)
data.put(4)
while not data.empty():
    print(data.get()) # Retrieve elements with .get()
