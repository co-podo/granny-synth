from package.GrannyKnob import GrannyKnob
class StateKnob(GrannyKnob):
    def __init__(self, paramName, defaultVal, rotateCallbacks = [], pressCallbacks = [], paramStates = []):
        super().__init__(paramName, defaultVal, rotateCallbacks, pressCallbacks)
        self.paramStates = paramStates
        self.stateIndex = paramStates.index(defaultVal)

    def rotate(self, direction):
        length = len(self.paramStates)

        if direction == 0:
            self.stateIndex = (length + (self.stateIndex - 1)) % length
        else:
            self.stateIndex = (length + (self.stateIndex + 1)) % length
        self.value = self.paramStates[self.stateIndex]
        
        super().rotate(direction)
        return self.value
        # rotate

    def press(self):
        super().press()
        #press