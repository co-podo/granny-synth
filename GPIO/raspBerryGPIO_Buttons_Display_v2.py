"""
KY040 Python Class
Martin O'Hanlon
stuffaboutcode.com


Additional code added by Conrad Storz 2015 and 2016
"""
from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD
from ky040 import KY040
import RPi.GPIO as GPIO
import os, time
from pythonosc import udp_client
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
import argparse


        


#test
if __name__ == "__main__":

    # print ('Program start.')

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
    # Init OSC
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1",
    help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=5005,
    help="The port the OSC server is listening on")
    args = parser.parse_args()
    client = udp_client.SimpleUDPClient(args.ip, args.port)
    
# lcd setup
    lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)
    mcp.output(3,1)     # turn on LCD backlight
    lcd.begin(20,4)
    lcd.setCursor(0,0)  # set cursor to first lane
    lcd.message( "Hello Soundnerd" ) #display current parameter
    lcd.setCursor(0,1) # set cursor to second lane
    lcd.message( "GRAINZZZ" ) 

# Physical GPIO Pins of Buttons - DO NOT CHANGE
    CLOCKPIN = 4
    CLOCKPIN1 = 17
    CLOCKPIN2 = 27
    CLOCKPIN3 = 22
    CLOCKPIN4 = 5
     
    DATAPIN = 21
    DATAPIN1 = 13
    DATAPIN2 = 19
    DATAPIN3 = 26
    DATAPIN4 = 6
    
    SWITCHPIN = 20 
    SWITCHPIN1 = 16
    SWITCHPIN2 = 12
    SWITCHPIN3 = 25
    SWITCHPIN4 = 24
    

    def rotaryChange(direction, clockpin):
        print ("turned - " + str(direction))
        print ("pin moved - " + str(clockpin))
        lcd.clear();
        lcd.setCursor(0,0)  # set cursor to first lane
        lcd.message( "0123456789 123456789" )
        lcd.setCursor(0,1)
        lcd.message( "filter")
        lcd.setCursor(0,2)
        lcd.message( "val")
        lcd.setCursor(0,3)
        lcd.message(str(direction))
        
        client.send_message("/rotation", direction)
        client.send_message("/button", clockpin)
    def switchPressed(pin):
        print ("button connected to pin:{} pressed".format(pin))
        

    GPIO.setmode(GPIO.BCM)
    button0 = KY040(CLOCKPIN, DATAPIN, SWITCHPIN, rotaryChange, switchPressed)
    button1 = KY040(CLOCKPIN1, DATAPIN1, SWITCHPIN1, rotaryChange, switchPressed)
    button2 = KY040(CLOCKPIN2, DATAPIN2, SWITCHPIN2, rotaryChange, switchPressed)
    button3 = KY040(CLOCKPIN3, DATAPIN3, SWITCHPIN3, rotaryChange, switchPressed)
    button4 = KY040(CLOCKPIN4, DATAPIN4, SWITCHPIN4, rotaryChange, switchPressed)

    print ('Launch switch monitor class.')

    button0.start()
    button1.start()
    button2.start()
    button3.start()
    button4.start()
    
    print ('Start program loop...')
    try:
        while True:
            sleep(10)
    finally:
        print ('Stopping GPIO monitoring...')
        button0.stop()
        button1.stop()
        button2.stop()
        button3.stop()
        button4.stop()
        lcd.lcd_clear()
        GPIO.cleanup()
        print ('Program ended.')

