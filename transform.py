from PIL import Image
import glob
from random import randrange
import os
import cv2


def resize():
    image_dir = "Images"
    image_list = []

    for dir in os.listdir(image_dir):
        cwd = "/Users/damolaolugboji/Desktop/code/Image Scrape/Images/"
        path = os.path.join(cwd, dir)
        print(path)
        for filename in glob.glob("{}/*.jpg".format(path)):
            im = cv2.imread(filename)
            image_list.append(im)

    success = 0
    fail = 0
    name = 0
    path = "/Users/damolaolugboji/Desktop/code/Image Scrape/Transformed"

    for image in image_list:
        try:
            img = cv2.resize(image, (1080, 1920))
            cv2.imwrite(os.path.join(path, "{}.jpg".format(str(name))), img)
            success += 1
            name += 1
        except:
            fail += 1


def crop():
    image_dir = "Images"
    image_list = []

    for dir in os.listdir(image_dir):
        cwd = "/Users/damolaolugboji/Desktop/code/Image Scrape/Images/"
        path = os.path.join(cwd, dir)
        print(path)
        for filename in glob.glob("{}/*.jpg".format(path)):
            im = cv2.imread(filename)
            image_list.append(im)

    output_list = []
    success = 0
    fail = 0
    name = 0
    path = "/Users/damolaolugboji/Desktop/code/Image Scrape/Cropped"

    for image in image_list:
        try:
            if image.shape[1] > 1500:
                partition = image.shape[1] // 3
                cropped_image = image[0 : image.shape[0], partition : (partition * 2)]
            cv2.imwrite(os.path.join(path, "{}.jpg".format(str(name))), cropped_image)
            success += 1
            name += 1
        except:
            fail += 1


def random_number():
    return str(randrange(100000))


if __name__ == "__main__":
    resize()
