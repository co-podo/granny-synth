from pythonosc import udp_client
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
import argparse

class GrannySynth:
    def __init__(self, grannyStates = [None, None, None, None], defaultState = None, viewManager = None):
        self.grannyStates = grannyStates
        self.currentState = defaultState

        parser = argparse.ArgumentParser()
        parser.add_argument("--ip", default="127.0.0.1",
        help="The ip of the OSC server")
        parser.add_argument("--port", type=int, default=5005,
        help="The port the OSC server is listening on")
        args = parser.parse_args()
        self.client = udp_client.SimpleUDPClient(args.ip, args.port)

    def pressKnob(self, knobIndex):
        if (knobIndex == 4):
            self.pressSpecial()
        else:
            knob = self.knobs[knobIndex]
            self.currentState.pressKnob(knobIndex)
        # change parameter names and values in display

    def rotateKnob(self, knobIndex, direction):
        if (knobIndex == 4):
            self.rotateStates(direction)
        else:
            knob = self.knobs[knobIndex]
            self.currentState.rotateKnob(knobIndex, direction)
            msg = "/" + self.currentState.name + "-" + knob.paramName
            self.client.send_message(msg, knob.value)
            print(msg + ": " + str(knob.value))
        # change parameter value in display

    @property
    def parameters(self):
        params = {}
        for state in self.grannyStates:
            params[state.name] = state.parameters
        return params

    @property
    def knobs(self):
        return self.currentState.knobs

    def rotateStates(self, direction):
        i = self.grannyStates.index(self.currentState)
        length = len(self.grannyStates)

        if direction == 0:
            self.currentState = self.grannyStates[(length + (i - 1)) % length]
        else:
            self.currentState = self.grannyStates[(length + (i + 1)) % length]

        self.currentState.view.display()

    def pressSpecial(self):
        pass
