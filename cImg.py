from PIL import Image
import os
from shutil import copyfile
from util import coordinate, MinMax

class SombraImg:

    def __init__(self, path, MCUInfo):
        self.path = path
        self.directory = os.path.dirname(path)
        self.filename = os.path.split(path)[1].rsplit('.',1)[0]
        self.extension = os.path.split(path)[1].rsplit('.',1)[1]
        self.MCUInfo = MCUInfo
        self.imgIsReady = False
        self.streamIsReady = False

    def close(self):
        self.Reload()

    def GetStream(self):
        self.OpenStream()
        return self.stream

    def OpenStream(self):
        if not self.streamIsReady:
            self.stream = open(self.path, 'r+b')
            self.streamIsReady = True

    def GetImg(self):
        self.OpenImg()
        return self.img

    def OpenImg(self):
        if not self.imgIsReady:
            self.img = Image.open(self.path).load()
            self.imgIsReady = True

    def Reload(self):
        if self.imgIsReady:
            self.img = None
            self.imgIsReady = False
        if self.streamIsReady:
            self.stream.close()
            self.streamIsReady = False

    def GetCopyImage(self, newPath):
        directory = os.path.dirname(newPath)
        if not os.path.exists(directory):
            os.makedirs(directory)
        copyfile(self.path, newPath)
       # print('Creating new file: ' + newPath)
        return SombraImg(newPath, self.MCUInfo)


    def Modify(self, adress, value):
        self.OpenStream()
        self.stream.seek(adress)
        self.stream.write(chr(value))
        self.Reload()

    def GetValueAt(self,adress):
        self.OpenStream()
        self.stream.seek(adress)
        return self.stream.read(1)

    def GetNewSombraImg(self, adress, value):

        fileAdress = self.filename + '_' + '%02x'%adress
        newPath = os.path.join(self.directory, fileAdress, fileAdress + '_' + '%02x'%value + '.' + self.extension )
        if os.path.isfile(newPath):
            return SombraImg(newPath, self.MCUInfo)
        else:
            newImg = self.GetCopyImage(newPath)
            newImg.Modify(adress,value)
            return newImg

    def ValidateCoordinate(self, c_coordinate):
        McuInfo = self.MCUInfo
        if c_coordinate.x < McuInfo.min.x:
            if c_coordinate.y > McuInfo.min.y:
                c_coordinate.y -= 1
                c_coordinate.x = McuInfo.max.x + c_coordinate.x - McuInfo.min.x + 1
            else:
                return coordinate(-1,-1)
        elif c_coordinate.x > McuInfo.max.x:
            if c_coordinate.y < McuInfo.max.y:
                c_coordinate.y += 1
                c_coordinate.x = McuInfo.min.x + c_coordinate.x - McuInfo.max.x - 1
            else:
                return coordinate(-1,-1)
        return c_coordinate
