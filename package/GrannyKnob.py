class GrannyKnob:
    def __init__(self, paramName = "", defaultVal = 0, rotateCallbacks = [], pressCallbacks = []):
        self.paramName = paramName
        self.value = defaultVal
        self.rotateCallbacks = rotateCallbacks
        self.pressCallbacks = pressCallbacks

    def rotate(self, direction):
        # rotate
        for callback in self.rotateCallbacks:
            callback(self.value)

        return self.value

    def press(self):
        for callback in self.pressCallbacks:
            callback(self.value)
        # press
        return self.sideParam

    @property
    def sideParam(self):
        return ""

    @sideParam.setter
    def sideParam(self, newVal):
        pass

    @property
    def parameter(self):
        param = {
            "name": self.paramName,
            "value": self.value,
            "sideParam": self.sideParam
        }
        return param