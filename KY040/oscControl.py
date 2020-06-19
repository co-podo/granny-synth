import RPi.GPIO as GPIO
from KY040 import KY040
import os, time
from pythonosc import udp_client
import argparse

# Init OSC

parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="127.0.0.1",
    help="The ip of the OSC server")
parser.add_argument("--port", type=int, default=5005,
    help="The port the OSC server is listening on")
args = parser.parse_args()

client = udp_client.SimpleUDPClient(args.ip, args.port)

# for x in range(10):
#     client.send_message("/filter", random.random())
#     time.sleep(1)

def readVolume():
    value = os.popen("amixer get PCM|grep -o [0-9]*%|sed 's/%//'").read()
    return int(value)
def rotaryChange(direction):
    try:    
	    client.send_message("/rotation", direction)
    except:
	    print ("not connected")

def switchPressed(SWITCHPIN):
     print ("button pressed")


 
if __name__ == "__main__":
 
    CLOCKPIN = 4                                        
    DATAPIN = 17
    SWITCHPIN = 27 
    
    CLOCKPIN1 = 22
    DATAPIN1 = 5
    SWITCHPIN1 = 6
    
    CLOCKPIN2 = 13 
    DATAPIN2 = 19
    SWITCHPIN2 = 26
    
    CLOCKPIN3 = 16
    DATAPIN3 = 20
    SWITCHPIN3 = 21
     
    CLOCKPIN4 = 23
    DATAPIN4 = 24
    SWITCHPIN4 = 25
    
   
   
    
    GPIO.setmode(GPIO.BCM)
    
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
 
    try:
        while True:
            time.sleep(0.05)
    finally:
        button0.stop()
    button1.stop()
    button2.stop()
    button3.stop()
    button4.stop()
    GPIO.cleanup()
