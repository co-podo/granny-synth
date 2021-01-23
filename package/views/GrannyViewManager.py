from lib.PCF8574 import PCF8574_GPIO
from lib.Adafruit_LCD1602 import Adafruit_CharLCD
import RPi.GPIO as GPIO
from pythonosc import udp_client
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
import argparse
class GrannyViewManager:
    def __init__(self):
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

        parser = argparse.ArgumentParser()
        parser.add_argument("--ip", default="127.0.0.1",
        help="The ip of the OSC server")
        parser.add_argument("--port", type=int, default=5005,
        help="The port the OSC server is listening on")
        args = parser.parse_args()
        client = udp_client.SimpleUDPClient(args.ip, args.port)
        
        # lcd setup
        self.lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)
        mcp.output(3,1)     # turn on LCD backlight
        self.lcd.begin(20,4)

    def changeDisplay(self, x, y, text):
        self.lcd.setCursor(x, y)
        self.lcd.message(text)
    