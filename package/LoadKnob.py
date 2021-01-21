from package.StateKnob import StateKnob
import os

class LoadKnob(StateKnob):
    def __init__(self, paramName, rotateCallbacks = [], pressCallbacks = []):
        files = []
        for file in os.listdir("./samples"):
            if file.endswith(".wav"):
                files.append(str(file))
        files = sorted(files)

        defaultVal = files[0]
        super().__init__(paramName, defaultVal, rotateCallbacks, pressCallbacks, paramStates = files)
    
    def press(self):
        # confirm -> load sample

        return self.sideParam
        #press

    @property
    def sideParam(self):
        return "confirm"