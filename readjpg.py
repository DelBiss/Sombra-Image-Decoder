
from cImg import SombraImg
from util import CompareRow, FixeGlitch, coordinate, MinMax, Glitch, Glitchs, SombraMessage, SombraGlitch, CompareResult
from cMCU import MCU, MCU_Info
import cScore
import os

imgs_folder = os.path.join("Reaper")
imgs_mod_folder = os.path.join("Reaper")
#imgs_mod_folder = os.path.join("Reaper", "sombra_25b6c")
#imgs_mod_folder = os.path.join("Reaper", "sombra_25b6c", "sombra_25b6c_04_25b6d")
#imgs_mod_folder = os.path.join("Reaper", "sombra_25b6d")


fix_folder = "Fix\\"
imgs = ['\\'+'tece_imgur','\\'+ 'sombra']
#imgs = ['\\'+'tece_imgur','\\'+ 'sombra_25b6c_04']
#imgs = ['\\'+'tece_imgur','\\'+ 'sombra_25b6c_04_25b6d_8b']
#imgs = ['\\'+'tece_imgur','\\'+ 'sombra']#_25b6d_8a']
extansion = '.jpg'


Glitchs = Glitchs()
#Glitchs.Add(Glitch(int("0x00025B6C", 0), coordinate(90,17)))# ['8a','8a','8a','8a','8a',]})
Glitchs.Add(Glitch(int("0x00025B6D", 0), coordinate(90,17)))# ['8a','8a','8a','8a','8a',]})
#Glitchs.Add(Glitch(int("0x00025B6E", 0), coordinate(91,17)))# ['8a','8a','8a','8a','8a',]})
#Glitchs.Add(Glitch(int("0x00025D27", 0), coordinate(98,17)))# ['8a','8a','8a','8a','8a',]})
sombra_msg = SombraMessage()
result=[]

McuInfo = MCU_Info(coordinate(0,0), coordinate(239,137),MinMax(0,2))
logFile = open( 'log_row' + '.txt','w')
#logFile = open( imgs_mod_folder + imgs[1] +'_log_p_' + '%02x'%(Glitchs.glitch[0].GetGlitchAddress())+'_'+ str(Glitchs.glitch[0].GetGlitchCoordinate().x) +'_'+ str(McuInfo.testRange.max) + '.txt','w')
ori_f =  SombraImg(imgs_folder+imgs[0]+extansion, McuInfo)
mod_f =  SombraImg(imgs_mod_folder+imgs[1]+extansion, McuInfo)

max_fix1 = 16
max_fix2 = 16

for y_row in range(0,20):
    score = CompareRow(y_row,ori_f, mod_f)
    msg = 'Row #' + str(y_row) + ': ' + score.Print()
    logFile.write(msg)
    print (msg)

score = CompareRow(17,ori_f, mod_f)
for s in score.score:
    print((s))
    logFile.write(s.Print())


#for glitch in Glitchs.glitch:
    #glitchRes = []
    #sombra_msg.Add(mod_f, glitch.GetGlitchAddress())
    #if not glitch.AsFix():
        #for addres1 in range(0,max_fix1):
            #for addres2 in range(0,max_fix2):
                #Get the replacing character
                #tryfix = (addres1*16) + addres2
                #print(tryfix)
                #if tryfix>254:
#                    break
                #Modify the image
                #newFile = FixeGlitch(ori_f, mod_f, glitch, tryfix)
                #newFile.close()


    #msg = Glitchs.glitch[0].result.Print()
    #print(msg)
    #logFile.write(msg)

ori_f.close()
mod_f.close()


logFile.close()