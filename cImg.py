import os
from shutil import copyfile

from PIL import Image

from util import coordinate


class SombraImage:
    def __init__(self, path, mcuInfo):
        # type: (str, mcuInfo) -> SombraImage
        """

        :rtype: SombraImage
        :param path: Path to the imagefile to use
        :param mcuInfo: Imformation on the MCU used by this Image
        """
        self.image = None
        self.bytesStream = None
        self.path = path
        self.directory = os.path.dirname(path)
        self.filename = os.path.split(path)[1].rsplit('.',1)[0]
        self.extension = os.path.split(path)[1].rsplit('.',1)[1]
        self.mcuInfo = mcuInfo

    def close(self):
        if self.image is not None:
            self.image = None
        if self.bytesStream is not None:
            self.bytesStream.close()
            self.bytesStream = None

    def GetStream(self):
        self.openBytesStream()
        return self.bytesStream

    def openBytesStream(self):
        if self.bytesStream is None:
            self.bytesStream = open(self.path, 'r+b')

    def getImage(self):
        self.openImage()
        return self.image

    def openImage(self):
        if self.image is None:
            self.image = Image.open(self.path).load()

    def reload(self):
        self.close()

    def createCopy(self, newPath):
        directory = os.path.dirname(newPath)
        if not os.path.exists(directory):
            os.makedirs(directory)
        copyfile(self.path, newPath)
       # print('Creating new file: ' + newPath)
        return SombraImage(newPath, self.mcuInfo)

    def modifyImage(self, adress, value):
        self.openBytesStream()
        self.bytesStream.seek(adress)
        self.bytesStream.write(chr(value))
        self.reload()

    def getValueAt(self, adress):
        self.openBytesStream()
        self.bytesStream.seek(adress)
        return self.bytesStream.read(1)

    def generateModifiedImage(self, iAdress, iNewValue):

        fileAdress = self.filename + '_' + '%02x' % iAdress
        newPath = os.path.join(self.directory, fileAdress, fileAdress + '_' + '%02x' % iNewValue + '.' + self.extension)
        if os.path.isfile(newPath):
            return SombraImage(newPath, self.mcuInfo)
        else:
            newImg = self.createCopy(newPath)
            newImg.modifyImage(iAdress, iNewValue)
            return newImg

    def ValidateMcuCoordinate(self, oCoordinate):
        if oCoordinate.x < self.mcuInfo.min.x:
            if oCoordinate.y > self.mcuInfo.min.y:
                oCoordinate.y -= 1
                oCoordinate.x = self.mcuInfo.max.x + oCoordinate.x - self.mcuInfo.min.x + 1
            else:
                return coordinate(-1,-1)
        elif oCoordinate.x > self.mcuInfo.max.x:
            if oCoordinate.y < self.mcuInfo.max.y:
                oCoordinate.y += 1
                oCoordinate.x = self.mcuInfo.min.x + oCoordinate.x - self.mcuInfo.max.x - 1
            else:
                return coordinate(-1,-1)
        return oCoordinate
