import os
import cv2
from os import walk, getcwd
import numpy as np



# Check if camera opened successf


def process_img(imgfile, frame, seq):
    image = cv2.resize(frame, (1280, 720), interpolation=cv2.INTER_LINEAR)
    cv2.imwrite('.\\Processed\\' + imgfile + str(seq) + '.jpg', image)
    image is None
    os.chdir("lanenet-lane-detection")
    os.system(
        'python ./test_lanenet.py --weights_path ./model/tusimple_lanenet_vgg/tusimple_lanenet_vgg.ckpt --image_path {}'.format('..\\Processed\\' + imgfile + str(seq) + '.jpg'))
    os.chdir('..')

wd = getcwd() + '\\Read\\'
for (dirpath, dirnames, filenames) in walk(wd):
    for file in filenames:
        cap = cv2.VideoCapture(wd + file)
        if (cap.isOpened() == False):
            print("Error opening video stream or file")
        seq = 0
        while (cap.isOpened()):
            seq += 1
            ret, frame = cap.read()
            if ret == True:
                if seq % 10 == 1:
                    process_img(file, frame, seq)

            else:
                break

        cap.release()
        cv2.destroyAllWindows()

