class coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "[" + str(self.x) + "," + str(self.y) + "]"

    def isValid(self):
        return self.x >= 0 and self.y >= 0


class MinMax:
    def __init__(self, iMin, iMax):
        self.min = min(iMin, iMax)
        self.max = max(iMin, iMax)

    def __str__(self):
        return "Range from [" + str(self.min) + " to " + str(self.max) + "] " + '(' + str(self.max - self.min) + ')'
