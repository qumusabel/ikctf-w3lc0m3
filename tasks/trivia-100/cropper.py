from PIL import Image
import sys

print(sys.argv)
img = Image.open(sys.argv[1])
for i in range(16):
    img_cr = img.crop((i*32, 0, (i+1)*32, 512))
    img_cr.save(chr(i+65) + '.png')