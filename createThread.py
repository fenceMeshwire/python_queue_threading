#!/usr/bin/env/python3

# Python 3.9.5

# createThread.py

# Purpose: Create a thread

# Dependencies
import time, threading

def basic_function():
    print('Starting the thread...')
    for counter in range(10):
        print(counter, time.time())
        time.sleep(1.5)
    print('End of thread')

# Main program
print('Main program')
thread = threading.Thread(target=basic_function)
thread.start()
print('End of main program')
