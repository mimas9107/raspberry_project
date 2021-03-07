import network
import time
from machine import Pin
##refer to https://hardliver.blogspot.com/2019/01/micropython-esp8266-micropyhton.html
def connWiFi(ssid, password):
    sta_if=network.WLAN(network.STA_IF)
    sta_if.active(True)
    while not sta_if.isconnected():
        sta_if.connect(ssid,password)
        time.sleep(5)
    ip = sta_if.ifconfig()[0]
    return ip,True
def blinkLed():
    Pin(2,Pin.OUT)
    time.sleep(0.2)
    Pin(2,Pin.IN)
    time.sleep(0.2)

if __name__=='__main__':
    pwd=input('please input the WiFi password:')
    ip,is_conn=connWiFi('justin_mimas_p30pro',pwd)
    while is_conn:
        print('IP address: '+ip)
        blinkLed()
