
import util

class MCU_Info:
    def __init__(self, cMin, cMax, TestRange):
        self.min = cMin
        self.max = cMax
        self.testRange = TestRange

class MCU:
    MCU_SIZE = 8

    def __init__(self, img, c_coordinate):

        self.coordinate = img.ValidateCoordinate(c_coordinate)
        self.pixel_coordinate = util.coordinate(self.coordinate.x * 8, self.coordinate.y * 8)
        self.filename = img.filename
        self.data = None
        self.GetStream(img)

    def GetStream(self, img):
        if self.data is None:
            self.data = []
            img_stream = img.GetImg()
            for y_row in range(0, MCU.MCU_SIZE):
                row = []
                for x_col in range(0,MCU.MCU_SIZE):
                    row.append(list(img_stream[self.pixel_coordinate.x + x_col, self.pixel_coordinate.y + y_row]))
                self.data.append(row)

        return self.data
