import math
import cScore
from cMCU import MCU
import util

def FixeGlitch(img1, img2, glitch, tryfix):
    fix_mod = img2.GetNewSombraImg(glitch.GetGlitchAddress(), tryfix)
    # test the images
    score = CompareResult(glitch.GetGlitchCoordinate(), img1, fix_mod)
    score.SetFixAttemp(tryfix)
    glitch.result.AddScore(score)
    return fix_mod

def CompareRow(mcu_y, img1, img2):
    score = cScore.RangeScore(util.MinMax(img1.MCUInfo.min.x, img1.MCUInfo.max.x))
    for x_col in range(img1.MCUInfo.min.x, img1.MCUInfo.max.x):
        score.AddScore(CompareImg(coordinate(x_col,mcu_y), img1, img2))
    return score

def CompareImg (mcu_coordinate, img1, img2 ):
    mcu1 = MCU(img1, mcu_coordinate)
    mcu2 = MCU(img2, mcu_coordinate)
    return ComparePixel(mcu1, mcu2)

def CompareResult(mcu_coordinate, img1, img2):
    score = cScore.RangeScore(img1.MCUInfo.testRange)
    for testOffset in range(img1.MCUInfo.testRange.min, img1.MCUInfo.testRange.max):
        test_coordinate = img1.ValidateCoordinate( coordinate(mcu_coordinate.x+testOffset, mcu_coordinate.y))
        score.AddScore(CompareImg (test_coordinate, img1, img2 ))
    return score

def ComparePixel(MCU1,MCU2):
    mcu_Score = cScore.MCUScore(MCU1.coordinate)
    for y_row1, y_row2 in zip(MCU1.data,MCU2.data):
        for x_col1, x_col2 in zip(y_row1, y_row2):
            pixel = cScore.PixelScore(coordinate(x_col1, y_row1))
            for band1, band2 in zip(x_col1, x_col2):
                pixel.Add(math.fabs(band1-band2)*3)
            mcu_Score.AddScore(pixel)
    return mcu_Score


class coordinate:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return "[" + str(self.x) + "," + str(self.y) + "]"
    def isValid(self):
        return self.x >= 0 and self.y >= 0

class MinMax:
    def __init__(self, iMin, iMax):
        self.min = min(iMin,iMax)
        self.max = max(iMin,iMax)

    def __str__(self):
        return "Range from [" + str(self.min) + " to " + str(self.max) + "] " + '('+ str(self.max - self.min) + ')'

class Glitchs:
    def __init__(self, ):
        self.glitch = []

    def Add(self, glitch):
        self.glitch.append(glitch)

class Glitch:

    def __init__(self, address, mcu_coordinate, fixs=[]):
        self.mcu_coordinate = mcu_coordinate
        self.address = address
        self.fixs = fixs
        self.result = cScore.GlitchScore(self)

    def __str__(self):
        return "MCU" + str(self.mcu_coordinate) + " @ 0x" + '%02x'%self.address

    def GetGlitchAddress(self):
        return self.address

    def GetGlitchCoordinate(self):
        return self.mcu_coordinate

    def AsFix(self):
        if len(self.fixs) > 0:
            return True
        return False

class SombraGlitch:
    def __init__(self,img, address):
        self.address = address
        self.character = img.GetValueAt(self.address)

class SombraMessage:

    def __init__(self):
        self.temperings = []

    def Add(self, img,address):
        self.temperings.append(SombraGlitch(img, address))

    def Read(self):
        msg = ''
        for char in self.temperings:
            msg += char.character

        return msg

