
import toAscii
import time
from PIL import Image

print('> Opening...')
f = open("./sandbox.txt", 'w')

frameCount = 5477 # run extractFrames.py and change it
for frame in range(1, frameCount + 1):
    f = open("./sandbox.txt", 'w')
    if frame >= 1000:
        f.writelines(toAscii.convert_image_to_ascii(Image.open('./frames/000{0}.bmp'.format(frame)), 50))
    elif frame >= 100:
        # more than 99
        f.writelines(toAscii.convert_image_to_ascii(Image.open('./frames/0000{0}.bmp'.format(frame)), 50))
    elif frame >= 10:
        # less than 100 but more than 9
        f.writelines(toAscii.convert_image_to_ascii(Image.open('./frames/00000{0}.bmp'.format(frame)), 50))
    else:
        # less than 10
        f.writelines(toAscii.convert_image_to_ascii(Image.open('./frames/000000{0}.bmp'.format(frame)), 50))

    f.close()
    print("{0}/{1}".format(frame, frameCount))
    #time.sleep(0.05)
    time.sleep(0.0548 / 3) # sync this