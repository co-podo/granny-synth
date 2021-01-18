class GrannySynth:
    def __init__(self):
        self.currentState = None

    def pressButton(self, buttonNumber):
        newState = self.buttons[buttonNumber].heldState
        self.currentState = newState

        print("state > " + self.currentState.name)
        # change parameter names and values in display

    def rotateButton(self, buttonNumber, direction):
        button = self.buttons[buttonNumber]
        button.rotate(direction)
        # change parameter value in display

    @property
    def buttons(self):
        return self.currentState.buttons

    @buttons.setter
    def buttons(self, b):
        self.currentState.buttons = b
