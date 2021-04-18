import os

print('> Extract Video')
os.system('./ffmpeg -i video.mp4 -vf "scale=480:360,fps=25" frames/%07d.bmp')
#os.system('./ffmpeg -i video.mp4 -vsync 0 frames/%07d.bmp')
print('> SUCCESS!')