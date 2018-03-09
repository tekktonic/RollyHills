"""Abstract away the terminal control sequences"""

from sys import stdin
import termios

TERMATTRS = None

def save():
    """Save the terminal state so that we can restore it at the end (called in game setup)"""
    global TERMATTRS
    TERMATTRS = termios.tcgetattr(stdin)

def restore():
    """Bring the terminal back to our original status"""
    global TERMATTRS
    termios.tcsetattr(stdin, termios.TCSANOW, TERMATTRS)
