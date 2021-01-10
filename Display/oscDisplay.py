#!/usr/bin/env python3
########################################################################
# Filename    : I2CLCD1602.py
# Description : Use the LCD display data
# Author      : freenove
# modification: 2018/08/03
########################################################################
from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD

from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
import argparse

from time import sleep, strftime
from datetime import datetime

def print_handler(address, *args):
    
    parameter = address.strip("/")

    print(f"{parameter}: {args}")
    lcd.setCursor(0,0)  # set cursor to first lane
    lcd.message( f"{parameter}" ) #display current parameter
    lcd.setCursor(0,1) # set cursor to second lane
    lcd.message( f"{args[0]}" ) 
    
    

def default_handler(address, *args):
    print(f"DEFAULT {address}: {args}")
 
def get_cpu_temp():     # get CPU temperature and store it into file "/sys/class/thermal/thermal_zone0/temp"
    tmp = open('/sys/class/thermal/thermal_zone0/temp')
    cpu = tmp.read()
    tmp.close()
    return '{:.2f}'.format( float(cpu)/1000 ) + ' C'
 
def get_time_now():     # get system time
    return datetime.now().strftime('    %H:%M:%S')
    
def loop():
         # set number of LCD lines and columns
    while(True):         
        #lcd.clear() 
        lcd.setCursor(0,0)  # set cursor position
        lcd.message( 'CPU:' )# display CPU temperature
        lcd.message( get_time_now() )   # display the time
        sleep(1)
        
def destroy():
    lcd.clear()
    
PCF8574_address = 0x27  # I2C address of the PCF8574 chip.
PCF8574A_address = 0x3F  # I2C address of the PCF8574A chip.
# Create PCF8574 GPIO adapter.
try:
    mcp = PCF8574_GPIO(PCF8574_address)
except:
    try:
        mcp = PCF8574_GPIO(PCF8574A_address)
    except:
        print ('I2C Address Error !')
        exit(1)
# Create LCD, passing in MCP GPIO adapter.


if __name__ == '__main__':
    
#     print ('Program is starting ... ')
#     print ('Program started! ')
    lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)
    mcp.output(3,1)     # turn on LCD backlight
    lcd.begin(16,2)
# 
#
    parameter = "default"
    dispatcher = Dispatcher()
    dispatcher.map("/filter/*", print_handler)
    dispatcher.set_default_handler(default_handler)
#
    
    ip = "127.0.0.1"
    port = 1337

    server = BlockingOSCUDPServer((ip, port), dispatcher)
    
    
    try:
        
        server.serve_forever() 
        ##loop()
        
    except KeyboardInterrupt:
        destroy()

