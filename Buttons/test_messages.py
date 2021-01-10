from pythonosc import udp_client
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
import argparse

 # Init OSC

parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="127.0.0.1",
help="The ip of the OSC server")
parser.add_argument("--port", type=int, default=5005,
help="The port the OSC server is listening on")
args = parser.parse_args()
    
    
client = udp_client.SimpleUDPClient(args.ip, args.port)

client.send_message("/rotation", 0)   # Send float message
#client.send_message("/button", 20)  # Send message with int, float and string
