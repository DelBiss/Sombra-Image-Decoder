import sys
import time
#import datetime
from datetime import tzinfo, timedelta, datetime
class USTimeZone(tzinfo):

    def __init__(self, hours, reprname, stdname, dstname):
        self.stdoffset = timedelta(hours=hours)
        self.reprname = reprname
        self.stdname = stdname
        self.dstname = dstname

    def __repr__(self):
        return self.reprname

    def tzname(self, dt):
        if self.dst(dt):
            return self.dstname
        else:
            return self.stdname

    def utcoffset(self, dt):
        return self.stdoffset #+ self.dst(dt)

    def dst(self, dt):
        
        return timedelta(0)

Eastern  = USTimeZone(-4, "Eastern",  "EST", "EDT")

def printAdress(adress):
    return hex(adress) + ' [' + str(adress)  +']'

def printShift(o,n):
    return hex(ord(o)) + ' -> ' + hex(ord(n))
def log(txt,file=None):
    timestamp = '[' + str(datetime.now(Eastern)).split('.')[0] + '] '#datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + '] '
    sys.stdout.write(timestamp+txt)
    sys.stdout.write('\n')
    if file is not None:
        file.write(timestamp+txt)
        file.write('\n')

sys.stdout.write('\n')
imgs_folder = 'Reaper/'
#imgs = ['blizz_imgur.jpg','tece_imgur.jpg']
#imgs = ['tece_imgur.jpg', 'sombra_imgur.jpg']
#imgs = ['blizz.jpg','tece_imgur.jpg']
imgs = ['blizz.jpg','gd.jpg']
orig = open(imgs_folder+imgs[0], 'rb')
new = open(imgs_folder+imgs[1], 'rb')
logFile = open('log.txt','w')
replaced_bytes = ''
count=0
count_dif=0
count_good=0
first=0
first_o='not found'
first_n='not found'
print_count=0
dif = []
lastdif = 0
end = 0
first = 0
log(imgs_folder+imgs[0] + " -> " + imgs_folder+imgs[1],logFile)
start=8031
generate_datamosh = True
new_pic=''
text_to_encode = list("People don't know how to datamosh")
dataIndex = 0

while 1:
    o = orig.read(1)
    if not o:
        break
    if count>start and dataIndex < len(text_to_encode):
        new_pic += text_to_encode[dataIndex]
        dataIndex+=1
    else:
        new_pic += o
    count=count+1
#for o,n in zip(orig.read()): #, n in zip(orig.read(), new.read()):
    
#    if o != n:
#        
#        replaced_bytes += o
#        count_dif=count_dif+1
#        if count>start and print_count<20:
#            if first==0:
#                first=count
#            lastdif = count
#            print_count=print_count+1
#            log(printAdress(count) + ' : ' + printShift(o,n),logFile)
#        if count>start and end==0:
#            if (lastdif+1) < count:
#                end = lastdif
#        lastdif = count
#    else:
#        count_good=count_good+1
    #count=count+1

#print(replaced_bytes)


    
log(imgs_folder+imgs[0] + " -> " + imgs_folder+imgs[1],logFile)
#log('Count Good: ' + str(count_good),logFile)
#log('Count Dif: ' + str(count))
#log('Last stream Diff: ' + printAdress(end),logFile)
#log('Lenght Diff: ' + str(end-first),logFile)
if generate_datamosh:
    replaced_bytesFile = open(imgs_folder+imgs[0] + '-'+imgs[1]+'-Result.jpg','w')
    replaced_bytesFile.write(new_pic)
    replaced_bytesFile.close()
    
#log(hex(ord(first_o)) + ' -> ' + hex(ord(first_n)))
logFile.close()
sys.stdout.write('\n')