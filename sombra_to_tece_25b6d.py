import os

from cImg import SombraImage
from glitch import Glitch, Glitchs, SombraMessage, FixeGlitch
from mcuPixelReader import MCU_Info
from mcuPixelReader.compare import CompareRow
from util import coordinate, MinMax

logFile = open('log_row' + '.txt', 'w')

imgs_folder = os.path.join("Reaper")
imgs_mod_folder = os.path.join("Reaper")
imgs = ['Reaper/tece_imgur', 'Reaper/sombra']
extansion = '.jpg'

glitch = Glitch(int("0x00025B6D", 0), coordinate(90, 17))

McuInfo = MCU_Info(coordinate(0, 0), coordinate(239, 137), MinMax(0, 2))

ori_f = SombraImage(imgs[0] + extansion, McuInfo)
mod_f = SombraImage(imgs[1] + extansion, McuInfo)

max_fix1 = 16
max_fix2 = 16

glitchRes = []

if not glitch.AsFix():
    for addres1 in range(0, max_fix1):
        for addres2 in range(0, max_fix2):
            tryfix = (addres1 * 16) + addres2
            print('Replacing byte at address {0} with {1}'.format('%02x'%glitch.address, '%02x'%tryfix))
            if tryfix > 254:
                break

            newFile = FixeGlitch(ori_f, mod_f, glitch, tryfix)
            newFile.close()

    msg = Glitchs.glitch[0].result.Print()
    print(msg)
    logFile.write(msg)

ori_f.close()
mod_f.close()

logFile.close()
