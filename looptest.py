#!/usr/bin/python3
import threading as th

keep_going = True
def key_capture_thread():
    global keep_going
    input()
    keep_going = False
    

def do_stuff():
    th.Thread(target=key_capture_thread, args=(), name='key_capture_thread', daemon=True).start()
    while keep_going:
        print('Press Enter to quit the process!')

do_stuff()
