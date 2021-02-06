from gpiozero import MCP3008, PWMLED
import time


VR = MCP3008(7)
l1 = MCP3008(0)
l2 = MCP3008(1)
l3 = MCP3008(2)
#VR = 0 
while True:
    # valVR = VR.value 
    # print('variable resistor:',valVR*100)
    print(l1.value, l2.value, l3.value)