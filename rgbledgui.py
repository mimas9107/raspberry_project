from tkinter import *
import RPi.GPIO as GPIO
from Yourbox import Linebox
# class RGBLED():
#     def __init__(self, win):
#         win.title('My RGBLED app')
#         win.geometry('300x200+50+50')

def on_closing():
    print('close')
    window.destroy()
    GPIO.cleanup()

if __name__ == '__main__':
    window = Tk()
    window.geometry('+50+50')
    sensor = Linebox(window)
    window.protocol('WM_DELETE_WINDOW', on_closing)
    window.mainloop()
