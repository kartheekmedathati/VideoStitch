import sys
import os

f = open('command_log', 'w')

for i in range(0,30):
    frame_folder = '_frames'+ str(i).zfill(2)
    if not os.path.exists(frame_folder):
        os.makedirs(frame_folder)
    cmd = 'ffmpeg -i ' + str(i).zfill(2)+'.mp4 -vf "select=eq(pict_type\,I),crop=1280:500:20:125" -vsync vfr '+ frame_folder + '/L00_%05d.jpg'
    os.system(cmd)
    f.write(cmd+'\n')
f.close()
