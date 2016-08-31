import math

import cScore
import mcuPixelReader
import util
from util import coordinate


def CompareRow(mcu_y, img1, img2):
    score = cScore.RangeScore(util.MinMax(img1.mcuInfo.min.x, img1.mcuInfo.max.x))
    for x_col in range(img1.mcuInfo.min.x, img1.mcuInfo.max.x):
        score.AddScore(CompareMCU(coordinate(x_col, mcu_y), img1, img2))
    return score


def CompareMCU(mcu_coordinate, img1, img2):
    mcu1 = mcuPixelReader.MCU(img1, mcu_coordinate)
    mcu2 = mcuPixelReader.MCU(img2, mcu_coordinate)
    return ComparePixel(mcu1, mcu2)


def CompareResult(mcu_coordinate, img1, img2):
    score = cScore.RangeScore(img1.MCUInfo.testRange)
    for testOffset in range(img1.MCUInfo.testRange.min, img1.MCUInfo.testRange.max):
        test_coordinate = img1.ValidateMcuCoordinate(coordinate(mcu_coordinate.x + testOffset, mcu_coordinate.y))
        score.AddScore(CompareMCU(test_coordinate, img1, img2))
    return score


def ComparePixel(MCU1, MCU2):
    mcu_Score = cScore.MCUScore(MCU1.coordinate)
    for y_row1, y_row2 in zip(MCU1.data, MCU2.data):
        for x_col1, x_col2 in zip(y_row1, y_row2):
            pixel = cScore.PixelScore(coordinate(x_col1, y_row1))
            for band1, band2 in zip(x_col1, x_col2):
                pixel.Add(math.fabs(band1 - band2) * 3)
            mcu_Score.AddScore(pixel)
    return mcu_Score
