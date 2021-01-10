"""
KY040 Python Class
Martin O'Hanlon
stuffaboutcode.com


Additional code added by Conrad Storz 2015 and 2016
"""

import RPi.GPIO as GPIO
from time import sleep
import os, time
from pythonosc import udp_client
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
import argparse



class KY040:

    CLOCKWISE = 0
    ANTICLOCKWISE = 1
    DEBOUNCE = 50

    def __init__(self, clockPin, dataPin, switchPin, rotaryCallback, switchCallback):
        #persist values
        self.clockPin = clockPin
        self.dataPin = dataPin
        self.switchPin = switchPin
        self.rotaryCallback = rotaryCallback
        self.switchCallback = switchCallback

        #setup pins
        GPIO.setup(clockPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(dataPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(switchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def start(self):
        GPIO.add_event_detect(self.clockPin, GPIO.FALLING, callback=self._clockCallback, bouncetime=self.DEBOUNCE)
        GPIO.add_event_detect(self.switchPin, GPIO.FALLING, callback=self.switchCallback, bouncetime=self.DEBOUNCE)

    def stop(self):
        GPIO.remove_event_detect(self.clockPin)
        GPIO.remove_event_detect(self.switchPin)
    
    def _clockCallback(self, pin):
        if GPIO.input(self.clockPin) == 0:
#         self.rotaryCallback()
            self.rotaryCallback(GPIO.input(self.dataPin), self.clockPin)
        """
            data = GPIO.input(self.dataPin)
            if data == 1:
                self.rotaryCallback(self.ANTICLOCKWISE)
            else:
                self.rotaryCallback(self.CLOCKWISE)
        
        self.rotaryCallback(GPIO.input(self.dataPin))
        """

    def _switchCallback(self, pin):
        """
        if GPIO.input(self.switchPin) == 0:
            self.switchCallback()
        """
        self.switchCallback()

#test
if __name__ == "__main__":

    print ('Program start.')
    # Init OSC

    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1",
    help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=5005,
    help="The port the OSC server is listening on")
    args = parser.parse_args()
    
    
    client = udp_client.SimpleUDPClient(args.ip, args.port)
    


    CLOCKPIN = 4
    CLOCKPIN1 = 17
    CLOCKPIN2 = 27
    CLOCKPIN3 = 22
    CLOCKPIN4 = 5
    
    
    DATAPIN = 6
    DATAPIN1 = 13
    DATAPIN2 = 19
    DATAPIN3 = 26
    DATAPIN4 = 21
    
    SWITCHPIN = 20 
    SWITCHPIN1 = 16
    SWITCHPIN2 = 12
    SWITCHPIN3 = 25
    SWITCHPIN4 = 24
    

    def rotaryChange(direction, clockpin):
        print ("turned - " + str(direction))
        print ("pin moved - " + str(clockpin))
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
            print ('Ten seconds...')
    finally:
        print ('Stopping GPIO monitoring...')
        button0.stop()
        button1.stop()
        button2.stop()
        button3.stop()
        button4.stop()
        GPIO.cleanup()
        print ('Program ended.')

