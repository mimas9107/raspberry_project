#!/usr/bin/python3
#http://stupidpythonideas.blogspot.com/2013/10/why-your-gui-app-freezes.html
from gpiozero import RGBLED,Button, LED, MCP3008
from time import sleep
from signal import pause
from random import randint,choice
from threading import Timer

# global x_led

def user_press(x_leds):
    # r = randint(0,100) / 100;
    # g = randint(0,100) / 100;
    # b = randint(0,100) / 100;
    # print("R={},G={},B={}".format(r,g,b));
    # led.color = (r, g, b);
    # global x_led
    x_led=choice(x_leds)    
    print(x_led)
    x_led.on()
    sleep(1)
    return x_led

    

def user_release(y_led):
    # global x_led
    y_led.off()

def system_repeat():
    mValue = m1.value
    print('可變電阻值',mValue)
    # led.color = (0,0,mValue)
    Timer(0.1,system_repeat).start()
    
    
if __name__ == '__main__':
    # global x_led
    button = Button(18);
    #led = RGBLED(red=17, green=27, blue=22);

    led1=LED(17)
    led2=LED(27)
    led3=LED(22)
    leds = [led1,led2,led3]
    m1 = MCP3008(7)
    system_repeat()
    # print(m1)
    # button.when_pressed = user_press(leds)  ## 註冊一個 func到 button物件. 當按下按鈕執行 user_press()
    # button.when_released = user_release()
    while True:
        if button.is_pressed:
            whichled = user_press(leds)
            user_release(whichled)
        else:
            continue    
    # pause();
