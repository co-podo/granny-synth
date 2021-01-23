from package.views.GrannyStateView import GrannyStateView
class GrannyState:
    def __init__(self, name = None, knobs = [None, None, None, None], viewManager = None):
        self.name = name
        self.knobs = knobs

        viewParamNames = []
        viewParamValues = []
        for knob in knobs:
            viewParamNames.append(knob.paramName)
            viewParamValues.append(knob.value)

        self.view = GrannyStateView(viewManager, name, viewParamNames, viewParamValues)

    def rotateKnob(self, knobIndex, direction):
        knob = self.knobs[knobIndex]
        value = knob.rotate(direction)
        self.view.displayParam(knobIndex, value)
        self.view.display()

    def pressKnob(self, knobIndex):
        knob = self.knobs[knobIndex]

    @property
    def parameters(self):
        params = []
        for knob in self.knobs:
            params.append(knob.parameter)
        return params