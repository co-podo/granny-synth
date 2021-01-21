from package.GrannyKnob import GrannyKnob
from package.util import clamp
class FloatKnob(GrannyKnob):
    def __init__(self, paramName, defaultVal, rotateCallbacks, pressCallbacks, minValue, maxValue, increments):
        super().__init__(paramName, defaultVal, rotateCallbacks, pressCallbacks)
        self.minValue = minValue
        self.maxValue = maxValue
        self.increments = increments
        self.incrIndex = 0      

    def rotate(self, direction):
        if (direction == 0):
            self.value -= self.increments[self.incrIndex]
        else:
            self.value += self.increments[self.incrIndex]

        super().rotate(direction)
        return self.value

    def press(self):
        length = len(self.increments)

        self.incrIndex = (length + (self.incrIndex - 1)) % length

        super().press()
        return self.sideParam
        #press

    @property
    def sideParam(self):
        return str(self.increments[self.incrIndex])