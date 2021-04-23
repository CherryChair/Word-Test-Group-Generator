import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('s1.jpg',0)
img_rgb = cv.imread('s1.jpg')
template = cv.imread('t1.jpg',0)
w, h = template.shape[::-1]

method = cv.TM_CCOEFF_NORMED
res = cv.matchTemplate(img,template,method)
# cv.normalize( res, res, 0, 1, cv.NORM_MINMAX, -1)
threshold = 0.915
loc = np.where( res >= threshold)
zipped = zip(*loc[::-1])
for i in [0]:
    pt1 = (loc[0][i] + h + 5, loc[1][i])
    pt2 = (loc[0][i+1] - 5, loc[1][i+1] + w)
    if pt1[1] > pt2[1] or  pt1[0] > pt2[0]:
        print("FUCK")
        exit()
    # cv.rectangle(img_rgb, pt1, pt2, (0,0,255), 1)
    cv.imwrite(f"images/results/1/cropped{i//2}.png", img_rgb[pt1[0]:pt2[0], pt1[1]:pt2[1]])
# for pt1 in zipped:
#     cv.rectangle(img_rgb, pt1, (pt1[0] + w, pt1[1] + h), (0,0,255), 1)
cv.imwrite('images/results/res.png',img_rgb)
