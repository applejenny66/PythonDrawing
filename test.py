
import shutil
import os
import numpy as np
import operator   
import cv2 as cv

filename = "K_298_1_2.png"
img = cv.imread(filename)
cv.imshow("1", img)
cv.waitKey(0)