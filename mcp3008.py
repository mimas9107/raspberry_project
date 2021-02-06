from gpiozero import MCP3008
import time

lm35 = MCP3008(0)
lightness = MCP3008(7)
mvalue = MCP3008(6)
temp=0
light=0
while True:
    for i in range(1,6):
        value = lm35.value
        temp = temp + value
        time.sleep(0.05)
    temp = temp/5    
    
    print('temperature: ',temp*3.3*100)
    
    for i in range(1,6):
        valuel = lightness.value
        light = light + valuel
        time.sleep(0.05)
    light = light/5
    print('lumin: ',light*100)
    
    m = mvalue.value
    print(m)

    time.sleep(1)
    temp = 0
    light = 0
