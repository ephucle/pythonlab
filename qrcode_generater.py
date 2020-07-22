from PIL import Image, ImageDraw
import qrcode
data = ''' 
https://pypi.org/project/qrcode/
What is a QR Code?
A Quick Response code is a two-dimensional pictographic code used for its fast readability and comparatively large storage capacity. The code consists of black modules arranged in a square pattern on a white background. The information encoded can be made up of any kind of data (e.g., binary, alphanumeric, or Kanji symbols)

import qrcode
img = qrcode.make('Some data here')

'''
img = qrcode.make(data)
img.save('Hoang_Le_P.png')

