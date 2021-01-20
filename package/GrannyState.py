class GrannyState:
    def __init__(self, name = None, knobs = [None, None, None, None]):
        self.name = name
        self.knobs = knobs
        
    def rotateKnob(self, knobIndex, direction):
        knob = self.knobs[knobIndex]

    def pressKnob(self, knobIndex):
        knob = self.knobs[knobIndex]

    @property
    def parameters(self):
        params = []
        for knob in self.knobs:
            params.append(knob.parameter)
        return params