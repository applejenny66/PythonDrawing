# utils.py
import os
import shutil
import cv2 as cv
import numpy as np


def jpgtopng(filename, savename):
    from PIL import Image
    im = Image.open(filename) # 'sunflower.jpg'
    im.save(savename) # 'sunflower.png'

def readcsv(filename):
    import csv
    with open (filename, 'r', newline='') as csvfile:
        rows = csv.reader(csvfile)
        count = 0

        for row in rows:
            if (count < 5):
                print (row)
            else:
                break
            count += 1

def ClearALL():
    dir_list = ['./monitor_fix', './sequence', './color_result', './fixpoint', './monitor_pic', \
                './painting', './points', './fix_result', "./patch", "./all_color/r_type", \
                "./all_color/g_type", "./all_color/b_type"]
    for dir_name in dir_list:
        shutil.rmtree(dir_name)  
        os.mkdir(dir_name)

def RemoveRedundant(rlist):
    tidy_list = []
    for i in range(0, len(rlist)):
        tmp_element = rlist[i][0]
        tidy_list.append(tmp_element)
    return (tidy_list)

def colornumber(filename):
    r = []
    g = []
    b = []
    color = []
    img = cv.imread(filename)
    img_size = img.shape
    for x in range(0, img_size[0]):
        for y in range(0, img_size[1]):
            tmp_r = img[x, y, 0]
            tmp_g = img[x, y, 1]
            tmp_b = img[x, y, 2]
            if (tmp_r not in r):
                r.append(tmp_r)
                g.append(tmp_g)
                b.append(tmp_b)
            else:
                if (tmp_g not in g):
                    r.append(tmp_r)
                    g.append(tmp_g)
                    b.append(tmp_b)
                else:
                    if (tmp_b not in b):
                        r.append(tmp_r)
                        g.append(tmp_g)
                        b.append(tmp_b)
    count = len(r) # number of total color
    for i in range(0, count):
        color.append((r[i], g[i], b[i]))
    return (count, r, g, b, color)
                
def GenColorImg(color, savename):
    #length = len(colorlist)
    #for i in range(0, len(colorlist)):
    img = np.zeros((100, 100, 3))
    for x in range(0, 100):
        for y in range(0, 100):
            img[x, y, 0] = color[0]
            img[x, y, 1] = color[1]
            img[x, y, 2] = color[2]
    cv.imwrite(savename, img)

def GenMonitorImg(img, colorlist, size, savename):
    for i in range(0, len(colorlist)):
        for x in range(0, size[0]):
            for y in range(0, size[1]):
                img[x, y, 0] = colorlist[i][0]
                img[x, y, 1] = colorlist[i][1]
                img[x, y, 2] = colorlist[i][2]
        cv.imwrite(savename, img)


def BlankImg(size):
    img = np.zeros((size[0], size[1], size[2]))
    for x in range(0, size[0]):
        for y in range(0, size[1]):
            img[x, y, 0] = img[x, y, 1] = img[x, y, 2] = 255
    return (img)

if __name__ == "__main__":
    """
    count = 0
    for name in os.listdir("./sequence/"):
        filename = "./sequence/" + name
        #filename = name
        save_name = filename.replace('jpg', 'png')
        jpgtopng(filename, save_name)
        count += 1
    """
    filename = "sunflower.png"
    count, r, g, b, color = colornumber(filename)
    print ("count: ", count)
    print ("color: ", color)