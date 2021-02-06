#!/usr/bin/python3
import threading
import sys

def getch():
    import termios
    import sys, tty
    def _getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    return _getch()

def input_thread(char):
    char.append(getch())

def do_stuff():
    char = []
    thread.start_new_thread(input_thread, (char,))
    i = 0
    while not char :
        i += 1

    print("i = " + str(i) + " char : " + str(char[0]))

do_stuff()