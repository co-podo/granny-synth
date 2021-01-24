class GrannyViewManager:
    def __init__(self, debug = False):
        self.lcd = None
        self.debug = debug

    def changeDisplay(self, x, y, text):
        if not self.debug:
            if not self.lcd == None:
                self.lcd.setCursor(x, y)
                self.lcd.message(text)

    

    
    