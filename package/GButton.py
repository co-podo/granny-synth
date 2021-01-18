class GButton:
    def __init__(self, buttonConfig):
        self.parameterName = buttonConfig["name"]
        self.paramType = buttonConfig.setdefault("type", "linear")
        self.value = buttonConfig["default"]
        self.heldState = buttonConfig["newState"]


        # can be solved with setdefault()...
        if (self.paramType == "linear" or self.paramType == "exponential"):    
            self.min = buttonConfig["min"]
            self.max = buttonConfig["max"]
            self.increment = buttonConfig["increment"]
            self.states = None
        elif (self.paramType == "state"):
            self.min = None
            self.max = None
            self.increment = None
            self.states = buttonConfig["states"]

        self.pressMessage = None


    # brauchen wir diese Funktion?
    def press(self):
        print(self.pressMessage)
        # send self.pressMessage

    def rotate(self, direction):
        if (self.paramType == "linear" or self.paramType == "exponential"):
            if direction == 0:
                self.value -= self.increment
            else:
                self.value += self.increment
        elif (self.paramType == "state"):
            i = self.states.index(self.value)
            length = len(self.states)
            if direction == 0:
                self.value = self.states[(length + (i + 1)) % length]
            else:
                self.value = self.states[(length + (i - 1)) % length]

        print(self.parameterName + ": " + str(self.value))
        # send self.value and self.parameterName to PD