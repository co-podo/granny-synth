class GrannySynth:
    def __init__(self, grannyStates = [None, None, None, None], defaultState = None, viewManager = None):
        self.grannyStates = grannyStates
        self.currentState = defaultState

    def pressKnob(self, knobIndex):
        if (knobIndex == 4):
            self.pressSpecial()
        else:
            knob = self.knobs[knobIndex]
            knob.press()
        # change parameter names and values in display

    def rotateKnob(self, knobIndex, direction):
        if (knobIndex == 4):
            self.rotateStates(direction)
        else:
            knob = self.knobs[knobIndex]
            self.currentState.rotateKnob(knobIndex, direction)
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

    def pressSpecial(self):
        pass
