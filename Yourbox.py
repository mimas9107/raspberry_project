from tkinter import *
from gpiozero import MCP3008
from threading import Timer
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class Linebox():
    def __init__(self,w):
        ## Set window main functions
        w.title('溫度和光線的感應')
        w.option_add('*font',('verdana',18,'bold'))
        w.option_add('*background','#068587')
        w.option_add('*foreground','#ffffff')
        
        ## Create sensor
        self.lightness = MCP3008(7)
        self.temperature = MCP3008(0)
        self.m = MCP3008(6)

        #firebase
        cred = credentials.Certificate("/home/mimas/myvenv2/mimas9107-rpi-firebase-adminsdk-ep2tv-0c940bf7c9.json")
        firebase_admin.initialize_app(cred, 
            {
            'databaseURL': 'https://mimas9107-rpi-default-rtdb.firebaseio.com'
            }
            )
        self.mcp3008Ref = db.reference('raspberrypi/MCP3008')

        ## Set the GUI attributes
        self.temperatureText = StringVar()
        self.lightnessText = StringVar()
        self.mvariable = StringVar()        
        
        ## Set the GUI
        mainFrame = Frame(w, borderwidth=2,relief=GROOVE,padx=100,pady=10)
        Label(mainFrame, text='室內溫度：').grid(row=0, column=0, sticky=E, padx=5, pady=20)
        Label(mainFrame, text='室內光線：').grid(row=1, column=0, sticky=E, padx=5, pady=20)
        Label(mainFrame, text='可變電阻：').grid(row=2, column=0, sticky=E, padx=5, pady=20)
        Label(mainFrame, textvariable=self.temperatureText).grid(row=0, column=1, sticky=E, padx=5, pady=20)
        Label(mainFrame, textvariable=self.lightnessText).grid(row=1, column=1, sticky=E, padx=5, pady=20)
        Label(mainFrame, textvariable=self.mvariable).grid(row=2, column=1, sticky=E, padx=5, pady=20)

        mainFrame.pack(padx=10, pady=10)

        ## Change the GUI attributes
        # self.temperatureText.set("100")
        # self.lightnessText.set("90")
        # self.mvariable.set("70")
        self.autoUpdate()

    def autoUpdate(self):
        self.tempValue = self.temperature.value * 3.3 * 100
        self.lightValue = self.lightness.value * 100
        self.mvalue = self.m.value * 100
        self.temperatureText.set('%.1f' % self.tempValue)
        self.lightnessText.set('%.1f' % self.lightValue)
        self.mvariable.set('%.1f' % self.mvalue)


        self.mcp3008Ref.update(
            {
                'temperature':self.tempValue,
                'brightness':self.lightValue,
                'm1':self.mvalue
            }
        )
        Timer(2, self.autoUpdate).start()
    
    def getInfo(self):
        return (self.mvalue, self.tempValue, self.lightValue)

    def __del__(self):
        self.lightness.close()
        self.temperature.close()
        self.m.close()
