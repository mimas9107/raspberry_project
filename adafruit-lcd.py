#!/usr/bin/python3
## 參考 https://learn.adafruit.com/drive-a-16x2-lcd-directly-with-a-raspberry-pi 
##
## Wiring Diagram

## First, connect the Cobbler power pins to the breadboard power rail. +5.0V 
## from the Cobbler goes to the red striped rail (red wire) 
## and GND from the cobbler goes to the blue striped rail (black wire)
#
## In order to send data to the LCD we are going to wire  it up as follows
#
##    Pin #1 of the LCD goes to ground
##    Pin #2 of the LCD goes to +5V
##    Pin #3 (Vo) connects to the middle of the potentiometer
##    Pin #4 (RS) connects to the Cobbler #22
##    Pin #5 (RW) goes to ground
##    Pin #6 (EN) connects to Cobbler #17
##    Skip LCD Pins #7, #8, #9 and #10
##    Pin #11 (D4) connects to cobbler #25
##    Pin #12 (D5) connects to Cobbler #24
##    Pin #13 (D6) connects to Cobber #23
##    Pin #14 (D7) connects to Cobber #18
##    Pin #15 (LED +) goes to +5V (red wire)
##    Pin #16 (LED -) goes to ground (black wire)
from subprocess import Popen, PIPE
from time import sleep
from datetime import datetime
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd
    
# Modify this if you have a different sized character LCD
lcd_columns = 16
lcd_rows = 2
    
# compatible with all versions of RPI as of Jan. 2019
# v1 - v3B+
lcd_rs = digitalio.DigitalInOut(board.D22)
lcd_en = digitalio.DigitalInOut(board.D17)
lcd_d4 = digitalio.DigitalInOut(board.D25)
lcd_d5 = digitalio.DigitalInOut(board.D24)
lcd_d6 = digitalio.DigitalInOut(board.D23)
lcd_d7 = digitalio.DigitalInOut(board.D18)
    
    
# Initialise the lcd class
lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
                                        lcd_d7, lcd_columns, lcd_rows)
    
# looking for an active Ethernet or WiFi device
def find_interface():
    find_device = "ip addr show"
    interface_parse = run_cmd(find_device)
    for line in interface_parse.splitlines():
        if "state UP" in line:
            dev_name = line.split(':')[1]
    return dev_name
    
# find an active IP on the first LIVE network device
def parse_ip():
    find_ip = "ip addr show %s" % interface
    find_ip = "ip addr show %s" % interface
    ip_parse = run_cmd(find_ip)
    for line in ip_parse.splitlines():
        if "inet " in line:
            ip = line.split(' ')[5]
            ip = ip.split('/')[0]
    return ip
    
# run unix shell command, return as ASCII
def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output.decode('ascii')
    
# wipe LCD screen before we start
lcd.clear()
    
# before we start the main loop - detect active network device and ip address
sleep(2)
interface = find_interface()
ip_address = parse_ip()
    
while True:
    
    # date and time
    lcd_line_1 = datetime.now().strftime('%b %d  %H:%M:%S\n')
    
    # current ip address
    lcd_line_2 = "IP " + ip_address
    
    # combine both lines into one update to the display
    lcd.message = lcd_line_1 + lcd_line_2
    
    sleep(2)
    lcd.clear()
    lcd.message = "hello!"
    sleep(2)