import os
import cv2
from os import walk, getcwd


def process_img(imgfile):
    image = cv2.imread('.\\Read\\' + imgfile, cv2.IMREAD_COLOR)
    image = cv2.resize(image, (1280, 720), interpolation=cv2.INTER_LINEAR)
    cv2.imwrite('.\\Processed\\' + imgfile, image)
    image is None
    os.chdir("lanenet-lane-detection")
    os.system(
        'python ./test_lanenet.py --weights_path ./model/tusimple_lanenet_vgg/tusimple_lanenet_vgg.ckpt --image_path {}'.format('..\\Processed\\' + imgfile))
    os.chdir('..')

wd = getcwd() + '\\Read\\'
for (dirpath, dirnames, filenames) in walk(wd):
    for file in filenames:
        process_img(file)
