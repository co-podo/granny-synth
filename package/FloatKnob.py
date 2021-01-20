from package.GrannyKnob import GrannyKnob
from package.util import clamp
class FloatKnob(GrannyKnob):
    def __init__(self, paramName, defaultVal, rotateCallbacks, pressCallbacks, minValue, maxValue, coarseIncr, fineIncr, interpol):
        super().__init__(paramName, defaultVal, rotateCallbacks, pressCallbacks)
        self.minValue = minValue
        self.maxValue = maxValue
        self.coarseIncr = coarseIncr
        self.fineIncr = fineIncr
        self.currIncr = self.coarseIncr
        self.interpol = interpol

    def rotate(self, direction):
        super().rotate(direction)

        if (direction == 0):
            self.value -= self.currIncr
        else:
            self.value += self.currIncr

        return self.value

    def press(self):
        super().press()
        if (self.currIncr == self.coarseIncr):
            self.currIncr = self.fineIncr
        else:
            self.currIncr = self.coarseIncr

        return self.sideParam
        #press

    @property
    def sideParam(self):
        if (self.currIncr == self.coarseIncr):
            return "coarse"
        return "fine"