from package.GrannyKnob import GrannyKnob
class StateKnob(GrannyKnob):
    def __init__(self, paramName, defaultVal, paramStates = []):
        super().__init__(paramName, defaultVal)
        self.paramStates = paramStates

    def rotate(self, direction):
        super().rotate(direction)

        i = self.paramStates.index(self.value)
        length = len(self.paramStates)

        if direction == 0:
            self.value = self.paramStates[(length + (i - 1)) % length]
        else:
            self.value = self.paramStates[(length + (i + 1)) % length]

        print(self.paramName + ": " + str(self.value))

        return self.value
        # rotate

    def press(self):
        super().press()
        #press