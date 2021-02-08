#!/usr/bin/python3

## Reference:
## [tkinter 8.5 doc] https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html
## 
import RPi.GPIO as GPIO
from gpiozero import LED
from tkinter import *
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class App():
    def __init__(self, main):
        #firebase
        cred = credentials.Certificate("/home/mimas/myvenv2/mimas9107-rpi-firebase-adminsdk-ep2tv-0c940bf7c9.json")
        firebase_admin.initialize_app(cred, 
            {
            'databaseURL': 'https://mimas9107-rpi-default-rtdb.firebaseio.com'
            }
            )
        self.ledControlRef = db.reference('raspberrypi/LED_Control')
        
        #print("main coming")
        main.title("Led control")
        ## window size+position: "width x height + pos_x + pos_y"
        main.geometry("300x200+50+50")  
        main.option_add("*Font",("verdana",18,"bold"))
        main.option_add("*Label.Font",("verdana",18))
        main.option_add("*Button.Background","dark gray")
        ## 建立mainFrame物件.
        mainFrame=Frame(main)  ## create a frame instance in the App. Frame object acts as spacer. 
        
        ## 在mainFrame物件中,建立按鈕物件, 並賦值於 App class的 "屬性": self.objectinstance = object().
        self.ledButton = Button(mainFrame, text="LED CLOSE關", padx=40,pady=40,command=self.userClick)
        ## 呼叫按鈕物件的 method : pack() 產生於視窗中.
        self.ledButton.pack(expand=YES)
        
        self.ledButton2= Button(mainFrame, text="blink",fg='blue', command=self.blinkgo)
        self.ledButton2.pack(expand=YES)
        
        ## 呼叫mainfram物件的 method : pack() 產生於視窗中.
        mainFrame.pack(expand=YES, fill=BOTH)
        self.ledState = False
        
    def userClick(self):
        #print("userClick")
        if self.ledState:
            self.ledState = False
            self.ledControlRef.update({"LED25":"CLOSE"})
            ##GPIO.output(GPIO25,GPIO.LOW)
            bigLed.off()
            self.ledButton.config(text="LED OPEN開")
        else:
            self.ledState = True
            self.ledControlRef.update({"LED25":"OPEN"})
            ##GPIO.output(GPIO25,GPIO.HIGH)
            bigLed.on()
            
            self.ledButton.config(text="LED CLOSE關")
            
    def blinkgo(self):
        for i in range(1,10):
            GPIO.output(GPIO25,GPIO.HIGH)
            self.ledButton2.config(text="blink %d times" % i)
            
            time.sleep(0.25)
            GPIO.output(GPIO25,GPIO.LOW)
            self.ledButton2.config(text="blink %d times" % i)
            self.ledButton2.flash()
            #time.sleep(0.25)
            
def on_closing():
    print("closing!")
    #GPIO.cleanup()
    window.destroy()


            
if __name__ == '__main__':
    GPIO25=25    
    bigLed = LED(GPIO25)
    ## GPIO.BCM: use board GPIO serial no#, eg. GPIO25 = pin22.
    #GPIO.setmode(GPIO.BCM) 
    #GPIO.cleanup()
    #GPIO.setwarnings(False)
    #GPIO.setup(GPIO25, GPIO.OUT)
    
    ## get instance from Tk class.
    window = Tk()  
    app = App(window)
    ## Warning: override the close event of main window.
    window.protocol("WM_DELETE_WINDOW", on_closing) 
    window.mainloop()