#!/usr/bin/python3
import RPi.GPIO as GPIO
from time import sleep, time
import datetime
from tkinter import *
from lcdwired import lcdwired
import mfrc522 as MFRC522
import threading
from gpiozero import Buzzer

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class App():
    def __init__(self, window):
        
        ## 初始化 lcd
        self.my_lcd = lcdwired()
        ## 初始化 Buzzer
        self.my_buzzer = Buzzer(16)
        ## 初始化 RFID
        self.previousUid=[] ##為了防止卡片放太久
        self.MIFAREReader = MFRC522.MFRC522()
        self.rfidStatusHandler()

        #firestore
        cred = credentials.Certificate("/home/mimas/myvenv2/mimas9107-rpi-firebase-adminsdk-ep2tv-0c940bf7c9.json")
        firebase_admin.initialize_app(cred, 
            {
            'databaseURL': 'https://mimas9107-rpi-default-rtdb.firebaseio.com'
            }
            )
        self.firestore = firestore.client()

    def rfidStatusHandler(self):
        ## create a thread to handle the rfid detect
        (status, tagType) = self.MIFAREReader.MFRC522_Request(self.MIFAREReader.PICC_REQIDL)
        if status == self.MIFAREReader.MI_OK:
            ## 有卡片！
            self.my_lcd.lcd_string('Found card',1); print('Found card')
            self.my_lcd.lcd_string('......',2)            
            self.cardRuning()                        
        else:
            ## 沒卡片！
            self.my_lcd.lcd_string('Put card on it',1); print('Put card on it')
            self.my_lcd.lcd_string('',2)

        
        # print('偵測rfid')
        threading.Timer.daemon=True
        threading.Timer(0.5, self.rfidStatusHandler).start()

    def cardRuning(self):
        ## 讀取狀態、UID
        (status, currentUid) = self.MIFAREReader.MFRC522_Anticoll()
        if status == self.MIFAREReader.MI_OK and currentUid != self.previousUid:
            self.previousUid = currentUid
            print(currentUid)
            cardCode = ''
            for singleID in currentUid:
                cardCode += '{:x}'.format(singleID)
            ## 輸出到 LCD
            self.my_lcd.lcd_string('Card ID',1)
            self.my_lcd.lcd_string(cardCode.upper(),2)
            ## 逼一聲！
            self.my_buzzer.on()
            sleep(0.4)
            self.my_buzzer.off()
            sleep(0.1)
            self.my_buzzer.on()
            sleep(0.1)
            self.my_buzzer.off()
            sleep(0.1)
            self.my_buzzer.on()
            sleep(0.1)
            self.my_buzzer.off()
            print(cardCode)
            self.saveToFireStore(cardCode)

    def saveToFireStore(self,cardCode):
        doc_ref = self.firestore.collection('Doors').document()
        currentTime = time()
        timestamp = datetime.datetime.fromtimestamp(currentTime)
        date = timestamp.strftime("%Y-%m-%d-%H-%M-%S")
        doc_ref.set({
            'timestamp':timestamp,
            'cardID':cardCode,
            'date':date
        })

def on_closing():
    GPIO.cleanup()
    root.destroy()



if __name__ == '__main__':
    GPIO.setwarnings(False) ##　關掉警告訊息。
    root = Tk()
    root.protocol('WM_DELETE_WINDOW',on_closing)

    app = App(root)
    root.mainloop()

