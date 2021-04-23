import cv2 as cv
import numpy as np
import os

from matplotlib import pyplot as plt


def get_test_images():
    return os.listdir("images/test/")

def get_task_temps():
    return os.listdir("images/temps/")

def write_task_to_dir(task_num, image, pt1_x, pt2_x, pt1_y, pt2_y):
    group_folder = 1
    path = "images/results/" + str(group_folder) + "/"
    if not os.path.exists(path):
            os.makedirs(path)
    directory = os.listdir(path)
    while task_num in directory:
        path = "images/results/" + str(group_folder) + "/"
        if not os.path.exists(path):
            os.makedirs(path)
            break
        directory = os.listdir(path)
        group_folder += 1
    cv.imwrite(path + task_num, image[pt1_x:pt2_x, pt1_y:pt2_y])


if __name__ == "__main__":
    test_pics = get_test_images()
    for image in test_pics:
        img = cv.imread("images/test/" + image, 0)
        img_rgb = cv.imread("images/test/" + image)
        template = cv.imread('images/temps/template.jpg',0)
        w, h = template.shape[::-1]
        method = cv.TM_CCOEFF_NORMED
        res = cv.matchTemplate(img,template,method)
        threshold = 0.95
        loc = np.where(res >= threshold)
        for i in range(0, len(loc[0]) - 1):
            pt1 = (loc[0][i] + h + 5, loc[1][i])
            pt2 = (loc[0][i+1] - 5, loc[1][i+1] + w)
            # cv.rectangle(img_rgb, pt1, pt2, (0,0,255), 1)
            write_task_to_dir(image.rsplit("_")[0] + ".png", img_rgb, pt1[0], pt2[0], pt1[1], pt2[1])
