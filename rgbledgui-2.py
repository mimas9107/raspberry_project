from tkinter import *
import RPi.GPIO as GPIO
from Yourbox import Linebox
from threading import Timer
import requests
from requests import ConnectionError, HTTPError, Timeout


headers ={
    "user-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0"
}
apiKey = "BMDRXVBWR84P7URB" ## write api authority key for thingspeak 

def on_closing():
    print('close')
    window.destroy()
    GPIO.cleanup()

def sendLineMessage(m, T, L):
    paras = {'value1':'{:8.2f}'.format(T),
             'value2':'{:8.2f}'.format(L),
             'value3':'{:8.2f}'.format(m)
            }
    response = requests.get("https://maker.ifttt.com/trigger/notify_line/with/key/bFJRg_iEGZJ6FSBLPJ1brr",
                  params=paras,
                  headers=headers)
    print("send Line message")

def doThingSpeak(m, L, T):
    print('sent thingSpeak')
    requests.get("https://api.thingspeak.com/update?api_key=%s&field1=%.2f&field2=%.2f" % (apiKey,L,m),
                 headers=headers)


def checkValue():
    m,T,L = sensor.getInfo()  
    print("info=",m, T, L)
    if m > 90:
        sendLineMessage(m, T, L)
    doThingSpeak(m, L, T)
    Timer.daemon = True    ## Daemon act as a manager to close the Timer.
    Timer(60,checkValue).start() ## recursive calling by forking another Timer

if __name__ == '__main__':
    window = Tk()
    window.geometry('+50+50')
    sensor = Linebox(window)

    checkValue()


    window.protocol('WM_DELETE_WINDOW', on_closing)
    window.mainloop()
