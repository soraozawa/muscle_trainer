class Counter:
    def __init__(self):
        self.count = 0
        self.position = "Neutral"

    def countup(self):
        self.count += 1

    def setNeutral(self):
        self.position = "Neutral"

    def setUpper(self):
        self.position = "Upper"

    def setLower(self):
        self.position = "Lower"
