import os, time
from pythonosc import udp_client
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
import argparse
import threading

class GrannyMediator:
    def __init__(self, grannySynth, grannyViewManager, debug = False):
        self.grannySynth = grannySynth
        self.grannyViewManager = grannyViewManager

        if not debug:
            self.setupCommunication()
        else:
            self.grannyViewManager.debug = True

    def clockpinToIndex(self, pin):
        clockpinToKnobIndex = {
            "4": 0,
            "17": 1,
            "27": 2,
            "22": 3,
            "5": 4
        }
        return clockpinToKnobIndex[str(pin)]

    def switchpinToIndex(self, pin):
        switchpinToKnobIndex = {
            "20": 0,
            "16": 1,
            "12": 2,
            "25": 3,
            "24": 4
        }
        return switchpinToKnobIndex[str(pin)]

    def rotation(self, index, direction):
        self.grannySynth.rotateKnob(index, direction)
        # self.client.send_message("/rotation", direction)

    def press(self, index):
        self.grannySynth.pressKnob(index)
        # self.client.send_message("/button", clockpin)

    def setupCommunication(self):
        from lib.Adafruit_LCD1602 import Adafruit_CharLCD
        from lib.PCF8574 import PCF8574_GPIO
        import RPi.GPIO as GPIO
        from lib.ky040 import KY040

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
        
        # lcd setup
        self.lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)
        self.grannyViewManager.lcd = self.lcd

        mcp.output(3,1)     # turn on LCD backlight
        self.lcd.begin(20,4)

        GPIO.setmode(GPIO.BCM)

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
            index = self.clockpinToIndex(clockpin)
            self.rotation(index, direction)
            
        def switchPressed(switchpin):
            index = self.switchpinToIndex(switchpin)
            self.press(index)
            print ("button connected to pin:{} pressed".format(switchpin))

        button0 = KY040(CLOCKPIN, DATAPIN, SWITCHPIN, rotaryChange, switchPressed)
        button1 = KY040(CLOCKPIN1, DATAPIN1, SWITCHPIN1, rotaryChange, switchPressed)
        button2 = KY040(CLOCKPIN2, DATAPIN2, SWITCHPIN2, rotaryChange, switchPressed)
        button3 = KY040(CLOCKPIN3, DATAPIN3, SWITCHPIN3, rotaryChange, switchPressed)
        button4 = KY040(CLOCKPIN4, DATAPIN4, SWITCHPIN4, rotaryChange, switchPressed)

        button0.start()
        button1.start()
        button2.start()
        button3.start()
        button4.start()

        def buttonLoop():
            try:
                while True:
                    time.sleep(0.1)
            finally:
                print ('Stopping GPIO monitoring...')
                button0.stop()
                button1.stop()
                button2.stop()
                button3.stop()
                button4.stop()
                self.lcd.clear()
                GPIO.cleanup()
                print ('Program ended.')

        thread = threading.Thread(target=buttonLoop)
        thread.start()