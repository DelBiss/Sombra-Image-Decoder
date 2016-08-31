import math
import operator

PONDERED = 0
AVERAGE = 1
MAX_VALUE = 2

PIXEL_SCORE = MAX_VALUE
MCU_SCORE = MAX_VALUE
RANGE_SCORE = MAX_VALUE

class Score(object):

    def __init__(self):
        self.InitData()

    def InitData(self):
        self.data = []
        self.score = []
        self.nb = 0
        self.averageWeight = 0.5
        self.maxWeight = 2
        self.weight = 1
        self.InitType()

    def InitType(self):
        self.type = PONDERED


    def SetWeight(self,value):
        self.weight = value

    def SetType(self, type):
        self.type = type

    def Add(self, value):
        self.data.append(value)
        self.nb += 1

    def AddScore(self,s):
        self.score.append(s)
        self.nb += 1

    def GetSum(self):
        sum = 0
        sum += math.fsum(self.data)
        for s in self.score:
            sum += s.GetScore()
        return sum

    def GetAverage(self):

        if  self.nb > 0:
            return self.GetSum()/self.nb
        else:
            return self.nb

    def GetMax(self):
        maxValue = 0
        if len(self.data):
            maxValue = max(self.data)
        for s in self.score:
            maxValue = max(maxValue,s.GetScore())
        return maxValue

    def GetScore(self):
        if self.type == AVERAGE:
            return self.GetAverage() * self.weight
        elif self.type == MAX_VALUE:
            return self.GetMax() * self.weight
        return ((self.GetAverage() * self.averageWeight) + (self.GetMax() * self.maxWeight)) * self.weight

    def GetScoreAsInt(self, precision = 0):
        return int(round(self.GetScore()*(10*precision+1),precision))

    def GetScoreAsHex(self,precision=0):
        return '%02x'%int(round(self.GetScore() * (10 * precision + 1), precision))

    def Print(self):
        return "Score: " + str(self.GetScore())

class PixelScore(Score):

    def __init__(self, c_coordinate):
        self.InitData()
        self.coordinate = c_coordinate

    def InitType(self):
        self.type = PIXEL_SCORE

class MCUScore(PixelScore):
    def InitType(self):
        self.type = MCU_SCORE

    def Print(self):
        return str(self) + '\n'

    def __str__(self):
        return str(self.coordinate) + " -> " + str(self.GetScore())

class RangeScore(Score):
    def __init__(self, testRange):
        self.InitData()
        self.testRange = testRange
        self.fixattem = -1

    def InitType(self):
        self.type = RANGE_SCORE

    def SetFixAttemp(self, value):
        self.fixattem = value
    def Print(self):
        txt = str(self) #+ '\n'
        #for s in self.score:
            #txt += s.Print() + '\n'
        return txt

    def __str__(self):
        return "RangeScore: " + str(self.testRange) + " -> " +'%02x'%self.fixattem + ' = ' + str(self.GetScore())

class GlitchScore(Score):
    def __init__(self, glitch):
        self.InitData()
        self.glitch = glitch

    def Print(self):
        txt = str(self) + '\n'
        scoredic = {}
        for s in self.score:
            if s.GetScoreAsInt(1) in scoredic:
                scoredic[s.GetScoreAsInt(1)].append(s)
            else:
                scoredic[s.GetScoreAsInt(1)] = [s]

        orderedlist = sorted(scoredic.items(),key=operator.itemgetter(0))
        count = 0
        for sr in orderedlist:
            txt += str(sr[0]) + ' -> '
            for so in sr[1]:
                txt += '%02x'%so.fixattem + "; "
            txt += '\n'
            #if count > 5:
                #break

        return txt

    def __str__(self):
        return "GlitchScore: " + str(self.glitch) + " " + str(self.GetScore())