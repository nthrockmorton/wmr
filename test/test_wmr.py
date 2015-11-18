import filecmp
from ..wmr import crop

def test_mvp():
    pass
    #Light chamber with White LEDs
    #Take a photo using picamera and save to a location
    #Crop photo to only include dial
    #Crop and binarize each digit from the dial
    #Save each digit separately
    #Paste each image of the digits into a single file separated by white space
    #Open Tesseract (external)
    #Command Tesseract to process single image of digits with -psm and nobatch parameters
    #Retrieve Tesseract output file
    #Read 6 digits from output file and save as integer

    #Light chamber with White and Green LEDs
    #Take a photo and save to a different location
    #Overlay a black circle onto the green-lit image
    #Overlay a circular mask onto the green-lit image
    #Locate average coordinate of red needle
    #Determine location of needle relative to center in degrees
    #Convert degrees into gallons

    #Combine needle location output with dial output to form single integer in gallons

def test_cropdigit():
    crop()
    assert filecmp.cmp("test/image/expected/hundredsImage.jpg", "test/image/actual/hundredsImage.jpg")
