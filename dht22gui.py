#!/usr/bin/python3
from threading import Timer
import Adafruit_DHT
from tkinter import *
import RPi.GPIO as GPIO

detecting = True

class DHT22GUI():
    def __init__(self,w):
        ## Set window main functions
        
        w.option_add('*font',('verdana',18,'bold'))
        w.option_add('*background','#068587')
        w.option_add('*foreground','#ffffff')
        
        ## Create sensor
        self.DHT_SENSOR = Adafruit_DHT.DHT22
        self.DHT_PIN = 26 ## GPIO18

        # #firebase
        # cred = credentials.Certificate("/home/mimas/myvenv2/mimas9107-rpi-firebase-adminsdk-ep2tv-0c940bf7c9.json")
        # firebase_admin.initialize_app(cred, 
        #     {
        #     'databaseURL': 'https://mimas9107-rpi-default-rtdb.firebaseio.com'
        #     }
        #     )
        # self.mcp3008Ref = db.reference('raspberrypi/MCP3008')

        ## Set the GUI attributes
        self.temperatureText = StringVar()
        self.humidityText = StringVar()
             
        
        ## Set the GUI
        mainFrame = Frame(w, borderwidth=2,relief=GROOVE,padx=100,pady=10)
        Label(mainFrame, text='室內溫度：').grid(row=0, column=0, sticky=E, padx=5, pady=20)
        Label(mainFrame, text='室內濕度：').grid(row=1, column=0, sticky=E, padx=5, pady=20)
        
        Label(mainFrame, textvariable=self.temperatureText).grid(row=0, column=1, sticky=E, padx=5, pady=20)
        Label(mainFrame, textvariable=self.humidityText).grid(row=1, column=1, sticky=E, padx=5, pady=20)
        

        mainFrame.pack(padx=10, pady=10)

        ## Change the GUI attributes
        # self.temperatureText.set("100")
        # self.lightnessText.set("90")
        
        self.autoUpdate()

    def autoUpdate(self):
        global detecting
        humidity, temperature = Adafruit_DHT.read_retry(self.DHT_SENSOR, self.DHT_PIN)
             
        self.temperatureText.set('%.1f *C' % temperature)
        self.humidityText.set('%.1f ' % humidity)
        

        # ## firebase update to database on the cloud.
        # self.mcp3008Ref.update(
        #     {
        #         'temperature':tempValue,
        #         'brightness':lightValue,
        #         'm1':mvalue
        #     }
        # )
        th = Timer(2, self.autoUpdate)
        th.start()
        if not detecting:
            th.join()
            detecting = False
        else:
            pass
        


## ===========================================================================================

def on_closing():
    global detecting
    detecting = False
    print('close')
    GPIO.cleanup()
    window.destroy()


if __name__ == '__main__':
    window = Tk()
    window.geometry('400x300+50+50')
    window.title('溫度 與 濕度偵測 by DHT22')
    app_dht22 = DHT22GUI(window)
    
    window.protocol('WM_DELETE_WINDOW', on_closing)

    window.mainloop()
    detecting = False
