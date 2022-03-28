# File timer0.py
import time
def timer(func, *args):  # Simplistic timing function
    start = time.time()
    for i in range(1000):
        func(*args)
    return time.time() - start  # Total elapsed time in seconds
