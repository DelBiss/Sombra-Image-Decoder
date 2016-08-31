#execfile('readjpg.py')

from cImg import SombraImg

class jpgReader:
    def __init__(self):
        self.jpgMarkers = {}

    def addJpgMarker(self, code, name, description, lenght):
        self.jpgMarkers[code] = {'name'}
        print (name + ': ' + code + ' -> ' + description + ' [' + str(lenght) + ']')

    def addMultipeJpgMarker(self, codeStart, codeEnd, name, description, lenght):
        i = 0
        for reservedCode in range(int(codeStart, 16), int(codeEnd, 16) + 1):
            self.addJpgMarker(hex(reservedCode), name + str(i), description, lenght)
            i += 1


class jpgMarker:
    def __init__(self, oJpgReader):
        pass

# Definition of JPEG Marker from: http://lad.dsc.ufcg.edu.br/multimidia/jpegmarker.pdf

oJpgReader = jpgReader()
oJpgReader.addJpgMarker('0xc0', 'SOF0', 'Baseline DCT', 'V')
oJpgReader.addJpgMarker('0xc1', 'SOF1', 'Extended sequential DCT', 'V')
oJpgReader.addJpgMarker('0xc2', 'SOF2', 'Progressive DCT', 'V')
oJpgReader.addJpgMarker('0xc3', 'SOF3', 'Lossless (sequential)', 'V')
oJpgReader.addJpgMarker('0xc5', 'SOF5', 'Differential sequential DCT', 'V')
oJpgReader.addJpgMarker('0xc6', 'SOF6', 'Differential progressive DCT', 'V')
oJpgReader.addJpgMarker('0xc7', 'SOF7', 'Differential lossless ', 'V')
oJpgReader.addJpgMarker('0xc9', 'SOF9', 'Extended sequential DCT', 'V')
oJpgReader.addJpgMarker('0xca', 'SOF10', 'Progressive DCT', 'V')
oJpgReader.addJpgMarker('0xcb', 'SOF11', 'Lossless (sequential)', 'V')
oJpgReader.addJpgMarker('0xcd', 'SOF13', 'Differential sequential DCT', 'V')
oJpgReader.addJpgMarker('0xce', 'SOF14', 'Differential progressive DCT', 'V')
oJpgReader.addJpgMarker('0xcf', 'SOF15', 'Differential lossless', 'V')

oJpgReader.addJpgMarker('0xfe', 'COM', 'Comment', 'V')
oJpgReader.addJpgMarker('0xcc', 'DAC', 'Define arithmetic conditioning table(s)', 'V')
oJpgReader.addJpgMarker('0xde', 'DHP', 'Define hierarchical progression', 'V')
oJpgReader.addJpgMarker('0xc4', 'DHT', 'Define Huffman table(s)', 'V')
oJpgReader.addJpgMarker('0xdc', 'DNL', 'Define number of lines', 4)
oJpgReader.addJpgMarker('0xdb', 'DQT', 'Define quantization table(s)', 'V')
oJpgReader.addJpgMarker('0xdd', 'DRI', 'Define restart interval', 4)
oJpgReader.addJpgMarker('0xd9', 'EOI', 'End of image', 0)
oJpgReader.addJpgMarker('0xdf', 'EXP', 'Expand reference image(s)', 0)

oJpgReader.addJpgMarker('0xd8', 'SOI', 'Start of image', 0)
oJpgReader.addJpgMarker('0xdA', 'SOS', 'Start of scan', 'V')
oJpgReader.addJpgMarker('0x01', 'TEM', 'For temporary use in arithmetic coding', 0)

oJpgReader.addJpgMarker('0xc8', 'JPG', 'Reserved for JPEG extensions', 'U')
oJpgReader.addMultipeJpgMarker('0xf0', '0xfd', 'JPG', 'Restart for JPEG extensions', 'U')

oJpgReader.addMultipeJpgMarker('0xe0', '0xef', 'APP', 'Restart for application use', 'V')
oJpgReader.addMultipeJpgMarker('0x02', '0xBF', 'RES', 'Reserved', 'U')



