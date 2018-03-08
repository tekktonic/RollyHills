

from sys import stdin
import termios

def save():
    global termattrs
    termattrs = termios.tcgetattr(stdin)

def restore():
    global termattrs
    termios.tcsetattr(stdin, termios.TCSANOW, termattrs)
