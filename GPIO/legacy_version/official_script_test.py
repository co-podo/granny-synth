# Import the module and threading
from pyky040 import pyky040
import threading
from time import *
import RPi.GPIO as GPIO



# Define your callback
def my_callback(self):
    print('Hello world! The scale position is {}'.format(self))
    
def my_swcallback():
    print('Hello world! you have clicked button{} '.format(self))

if __name__ == "__main__":
    
    # Init the encoder pins
    my_encoder = pyky040.Encoder(CLK=4, DT=21, SW=20)
    

    # Or the encoder as a device (must be installed on the system beforehand!)
    # my_encoder = pyky040.Encoder(device='/dev/input/event0')

    # Setup the options and callbacks (see documentation)
    my_encoder.setup(scale_min=0, scale_max=100, step=1, chg_callback=my_callback, sw_callback=my_swcallback)
   

    # Create the thread
    my_thread = threading.Thread(target=my_encoder.watch)
    

    # Launch the thread
    my_thread.start()
    

    # Do other stuff
    print('Other stuff...')
    while True:
        print('Looped stuff...')
        my_encoder2 = pyky040.Encoder(CLK=17, DT=13, SW=16)
        my_encoder2.setup(scale_min=0, scale_max=100, step=1, chg_callback=my_callback, sw_callback=my_swcallback)
        my_thread2 = threading.Thread(target=my_encoder2.watch)
        my_thread2.start()
        sleep(1000)
       
