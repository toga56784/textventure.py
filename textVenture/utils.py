import sys
import time

def slow_print(s, d=0.1):
    """
    Print text to the terminal one character at a time with a delay.

    Args:
        s (str): The string to print.
        d (float): Time in seconds to wait between characters. Defaults to 0.1.

    Returns:
        None
    """
    for c in s:
        print(c, end='', flush=True)
        time.sleep(d)
    print()

def vert_print(s, d=0):
    """
    Prints text one character at a time vertically with an optional delay.

    Args:
        s (str): The string to print.
        d (float, optional): Time in seconds to wait between characters. Defaults to 0.
    
    Returns:
        None
    """
    for c in s:
        print(c)
        time.sleep(d)

def kill():
    """
    Imediately ends the session.

    Returns:
        None
    """
    print("Session terminated.")
    sys.exit()