import sys
import time

def slow_print(s, d):
    for c in s:
        print(c, end='', flush=True)
        time.sleep(d)