from SimpleCV import Image

#Hundreds place
def crop():
    #Begin Processing image
    print ('Begin processing image...')
    fullImage = Image('test/image/expected/fullImage.jpg')
    hundreds = fullImage.crop(602, 239, 28, 63)
    hundreds = hundreds.binarize(65).invert()
    hundreds.save('test/image/actual/hundredsImage.jpg')
    print ('Hundreds place cropped, binarized, and saved')
