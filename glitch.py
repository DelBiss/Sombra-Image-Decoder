import cScore
from mcuPixelReader.compare import CompareResult


def FixeGlitch(img1, img2, glitch, tryfix):
    fix_mod = img2.generateModifiedImage(glitch.GetGlitchAddress(), tryfix)
    # test the images
    score = CompareResult(glitch.GetGlitchCoordinate(), img1, fix_mod)
    score.SetFixAttemp(tryfix)
    glitch.result.AddScore(score)
    return fix_mod


class Glitchs:
    def __init__(self, ):
        self.glitch = []

    def Add(self, glitch):
        self.glitch.append(glitch)

class Glitch:
    def __init__(self, address, mcu_coordinate, fixs=None):
        if fixs is None:
            fixs = []
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
        self.character = img.getValueAt(self.address)

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

