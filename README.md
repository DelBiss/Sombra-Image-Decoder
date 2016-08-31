# Sombra-Image-Decoder

Script to decode Sombra Reaper Datamosh

## The Plan

Reverting change Sombra made will give us is message

## What can be done with this script

This script contain those class:
#### SombraImage
  * Open an image file in 2 format: File and Image
  * Create an new image with a modification to a specific adress into the image

#### mcuPixelReader
  * Refer to a MCU of an img
    * Return an Square array containing the RGB value of each pixel

#### mcuPixelReader Compare
  * Create a score from comparing 2 differents images based on RGB difference of each pixel.
  * Multiple way to compare
    * *CompareMCU*
      * Compare 2 MCU
    * *CompareRange*
      * Compare multiple MCU in a certain range of a specific MCU.
    * *ComparePixel*
      * Compare difference in RGB value for each pixel of a MCU
    * *CompareRow*
      * Compare all MCU in a specific Row

#### Score
  * Use to contain all the value to calculate a score.
  * Can calculate score by Average, Max_Value or Pondered
  * Print score in a readeable fashion
  * Contain sub-class for different type of score:
    * *PixelScore*
      * Create a score based on the difference of RGB value
    * *MCUScore*
      * Create a score from PixelScore
    * *RangeScore*
      * Create a score for multiple MCUScore

## State of decoding
For the first byte we've think have been modified, we've create the 256 variation of the byte and calculate a comparative score based on RGB value to find the most appropriate. The change with the best score didn't give the best visual result. It correct the huge difference in luminosity but the color isn't right.

For better result, it will be attemped to decrypt the hauffman table and compare DCT instead of RGB value. It will allow for a better comparaison and allow to find the change to make. It may not be the byte we've identified.

Because there is small value in the High Frequency that wasn't there in the tece image, it will also be attemped to modify the quantization table.

## In Progress
* Finding all the marker in the image.
