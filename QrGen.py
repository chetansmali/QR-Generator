#import qrcode
#import Image

import qrcode

#pass any link or any message it will convert into QR code

img=qrcode.make("https://www.servicecaart.com/")

#this will save the Qrcode image in current floder. 
img.save("servicecaart.jpg")