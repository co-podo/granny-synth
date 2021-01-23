class GrannyStateView:
    def __init__(self, viewManager, name = "name", paramNames = ["par1", "par2", "par3", "par4"], paramValues = ["val1", "val", 0, 0]):
        self.lineSize = 20
        self.lines = 4
        self.paramSizes = [5, 4, 4, 4]
        self.namePosition = int((self.lineSize / 2) - 3)
        self.lineNames = ["stateName", "paramNames", "paramValues", "empty"]
        self.borderThickness = 1
        self.paramLine = 2
        self.displayText = ["--------------------", "-----|----|----|----", "-----|----|----|----", "--------------------"]
        self.empty = " "

        self.viewManager = viewManager

        self.initDisplay(name, paramNames, paramValues)

    def changeParam(self, index, value, line = 2):
        y = line
        x = 0
        for paramIndex in range(index):
            x += self.paramSizes[paramIndex] + self.borderThickness

        size = self.paramSizes[index]
        value = str(value)[:size]
        value = value.rjust(size, self.empty)

        self.displayText[y] = self.displayText[y][0:x] + value + self.displayText[y][x+size:]

        self.viewManager.changeDisplay(x, y, value)
        # DELETE LATER ONLY FOR TESTING
        # self.display()

    def display(self):
        fullText = ""
        for line in self.displayText:
            fullText += line + "\n" # DELETE LINEBREAK LATER
        # GPIO

        self.viewManager.changeDisplay(0, 0, fullText)
        print(fullText)

    def initDisplay(self, name = "name", paramNames = ["par1", "par2", "par3", "par4"], paramValues = ["val1", "val", 0, 0]):          

        # name
        nameLine = self.emptyLine()
        nameLine = (nameLine[:self.namePosition] + name).ljust(self.lineSize, self.empty)
        self.displayText[self.lineNames.index("stateName")] = nameLine

        # paramNames
        for index in range(len(paramNames)):
            lineNumber = self.lineNames.index("paramNames")
            paramName = paramNames[index].ljust(self.paramSizes[index], self.empty)
            self.changeParam(index, paramName, lineNumber)

        # paramValues
        for index in range(len(paramValues)):
            lineNumber = self.lineNames.index("paramValues")
            paramValue = paramValues[index]
            self.changeParam(index, paramValue, lineNumber)
            
        # empty line
        self.displayText[self.lineNames.index("empty")] = self.emptyLine()
        self.display()


    def emptyLine(self):
        return "".ljust(self.lineSize, self.empty)