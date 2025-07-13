import sys
import time

def slow_print(s, d=0.1):
    for c in s:
        print(c, end='', flush=True)
        time.sleep(d)

def vert_print(s, d=None):
    for c in s:
        print(c)
        time.sleep(d)

def kill():
    print("Session terminated.")
    sys.exit()