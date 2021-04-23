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
    directory = os.listdir("images/results/" + str(group_folder) + "/")
    task_name = task_num
    # while task_name in directory:
    #     group_folder += 1
    #     directory = os.listdir("images/results/" + str(group_folder) + "/")
        
    cv.imwrite(f"images/results/" + str(group_folder) + "/" + task_num, image[pt1_x:pt2_x, pt1_y:pt2_y])


if __name__ == "__main__":
    temps = get_task_temps()
    test_pics = get_test_images()
    for image in test_pics:
        img = cv.imread("images/test/" + image, 0)
        img_rgb = cv.imread("images/test/" + image)
        for template_name in temps:
            template = cv.imread('images/temps/' + template_name,0)
            w, h = template.shape[::-1]
            method = cv.TM_CCOEFF_NORMED
            res = cv.matchTemplate(img,template,method)
            cv.normalize( res, res, 0, 1, cv.NORM_MINMAX, -1)
            threshold = 0.95
            loc = np.where( res >= threshold)
            zipped = zip(*loc[::-1])
            for i in [2*j for j in range(0, len(loc[0])//2)]:
                pt1 = (loc[0][i], loc[1][i])
                pt2 = (loc[0][i+1], loc[1][i+1] + w)
                if pt1[1] > pt2[1] or  pt1[0] > pt2[0]:
                    print("FUCK")
                    break
                # cv.rectangle(img_rgb, pt1, pt2, (0,0,255), 1)
                task_num = template_name.rsplit("_")[1]
                # cv.imwrite(f"images/" + task_num + "/" + task_num + ".png", img_rgb[pt1[0]:pt2[0], pt1[1]:pt2[1]])
                write_task_to_dir(task_num, img_rgb, pt1[0], pt2[0], pt1[1], pt2[1])
            # for pt1 in zipped:
            #     cv.rectangle(img_rgb, pt1, (pt1[0] + w, pt1[1] + h), (0,0,255), 1)
            # cv.imwrite('images/res.png',img_rgb)
