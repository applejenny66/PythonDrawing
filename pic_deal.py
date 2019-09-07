# pic_deal.py
# sunflower.jpg

import os
import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt

symbol_color = np.zeros((100, 100, 3))
name = "sunflower"
filename = name + ".jpg"
img = cv.imread(filename)
Z = img.reshape((-1,3))
Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 6
ret,label,center=cv.kmeans(Z,K,None,criteria,10,cv.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

cv.imwrite("1.png", res2)
print ("finished")
size = res2.shape
print ("size: ", size) # (399, 600, 3)

#### show the (r, g, b) color
color_r = []
color_g = []
color_b = []
color = []
for i in range(0, size[0]):
    for j in range(0, size[1]):
        tmp_r = res2[i, j, 0]
        tmp_g = res2[i, j, 1]
        tmp_b = res2[i, j, 2]
        if (tmp_r not in color_r):
            if (tmp_g not in color_g):
                if (tmp_b not in color_b):
                    color_r.append(tmp_r)
                    color_b.append(tmp_b)
                    color_g.append(tmp_g)

for x in range(0, len(color_r)):
    tmp_color = (color_r[x], color_g[x], color_b[x])
    color.append(tmp_color)

total_list = []
save_list = []
count = 1
while K > 0:
    for i in range(0, 100):
        for j in range(0, 100):
            symbol_color[i, j, 0] = color_r[count - 1]
            symbol_color[i, j, 1] = color_g[count - 1]
            symbol_color[i, j, 2] = color_b[count - 1]
            symbol_total = symbol_color[i, j, 0] + symbol_color[i, j, 1] + symbol_color[i, j, 2]
    save_name = str(color_r[count - 1]) + "_" + str(color_g[count - 1]) + "_" + str(color_b[count - 1]) + ".png"
    save_name = "./color_result/" + save_name
    cv.imwrite(save_name, symbol_color)
    count += 1
    K -= 1
    save_list.append(save_name)
    total_list.append(symbol_total)

print (save_list)
print (total_list)
count_ = 1
for i in range(0, len(total_list)):
    max_color = max(total_list)
    max_index = total_list.index(max_color)
    max_name = save_list[max_index]
    tmp_img = cv.imread(max_name)
    save_name = "./sequence/" + str(count_) + ".jpg"
    cv.imwrite(save_name, tmp_img)
    count_ += 1
    total_list.remove(max_color)
    save_list.remove(max_name)

#print ("color: ", color)
#print ("r: ", color_r)
#print ("g: ", color_g)
#print ("b: ", color_b)

print ("color: ", color)
print ("r: ", color_r)
print ("g: ", color_g)
print ("b: ", color_b)

img = cv.imread("1.png")
cover_img = np.zeros(size)
for m in range(0, size[0]):
    for n in range(0, size[1]):
        for p in range(0, size[2]):
            cover_img[m, n, p] = 255

for i in range(1, 7):
    sequence_name = "./sequence/" + str(i) + ".jpg"
    print (sequence_name)
    tmp_img = np.zeros(size)
    for m in range(0, size[0]):
        for n in range(0, size[1]):
            for p in range(0, size[2]):
                tmp_img[m, n, p] = 255
    tmp_color_img = cv.imread(sequence_name)
    tmp_color = tmp_color_img[10, 10]
    print ("tmp color: ", tmp_color)
    for x in range(0, size[0]):
        for y in range(0, size[1]):
            if (tmp_color[0] == img[x, y, 0]):
                if (tmp_color[1] == img[x, y, 1]):
                    if (tmp_color[2] == img[x, y, 2]):
                        tmp_img[x, y] = tmp_color
                        cover_img[x, y] = tmp_color

    save_name = "./monitor_pic/" + str(i) + ".jpg"
    cv.imwrite(save_name, tmp_img)
    save_name_2 = "./monitor_pic/" + str(i) + "_cover.jpg"
    cv.imwrite(save_name_2, cover_img)
    
    



