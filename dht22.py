#!/usr/bin/python3
import threading as th
import Adafruit_DHT
DHT_SENSOR = Adafruit_DHT.DHT22
#DHT_PIN = 18 ## GPIO18
DHT_PIN = 26
keep_going = True
def key_capture_thread():
    global keep_going
    input()
    keep_going = False

def detecting():
    print('================= Press Enter to quit the process! ===================')
    th.Thread(target=key_capture_thread, args=(), name='key_capture_thread', daemon=True).start()
    while keep_going:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        if (humidity is not None) & (temperature is not None):
            print('Temperature={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity))
        else:
            print('Failed to retrieve data from DHT sensor')
            break
    th.Thread(target = key_capture_thread, name='key_capture_thread')._stop()    

detecting()

    
    
