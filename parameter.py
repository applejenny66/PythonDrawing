# parameter.py
from utils import colornumber
import numpy as np
import cv2 as cv
from utils import ClearALL
import operator

def Kdetermine(count, r, g, b, color):
    r_type = []
    g_type = []
    b_type = []
    for i in range(0, count):
        tmp_list = [r[i], g[i], b[i]]
        tmp_max = max(tmp_list)
        tmp_index = tmp_list.index(tmp_max)
        if (tmp_index == 0):
            r_type.append(tmp_list)
        elif (tmp_index == 1):
            g_type.append(tmp_list)
        elif (tmp_index == 2):
            b_type.append(tmp_list)
        else:
            print ("there's error at", str(i))
    #print ("r type: ", r_type)
    #print ("g type: ", g_type)
    #print ("b type: ", b_type)
    return (r_type, g_type, b_type)

def GenTypeImg(colorlist, colortype):
    for i in range(0, len(colorlist)):
        img = np.zeros((100, 100, 3))
        color = colorlist[i]
        for x in range(0, 100):
            for y in range(0, 100):
                img[x, y, 0] = color[0]
                img[x, y, 1] = color[1]
                img[x, y, 2] = color[2]
        save_name = "./all_color/" + str(colortype) + "/" + str(i) + ".png"
        cv.imwrite(save_name, img)

def CompareSimilarImg():
    common_name = "./all_color/b_type/"
    color_list = []
    for i in range(4, 21):
        filename = common_name + str(i) + ".png"
        img = cv.imread(filename)
        r, g, b = img[10, 10, 0], img[10, 10, 1], img[10, 10, 2]
        color_list.append((r, g, b))
    return (color_list)

def CompareDistance(colorlist):
    distance_list = [] # square plus together
    for i in range(0, len(colorlist)-1):
        tmp_dist = (colorlist[i][0] - colorlist[i+1][0])*(colorlist[i][0] - colorlist[i+1][0]) + \
                    (colorlist[i][1] - colorlist[i+1][1])*(colorlist[i][1] - colorlist[i+1][1]) + \
                    (colorlist[i][2] - colorlist[i+1][2])*(colorlist[i][2] - colorlist[i+1][2])
        distance_list.append(tmp_dist)
    return (distance_list)

def SortColor(colorlist):
    total_color_dict = {}
    for i in range(0, len(colorlist)-1):
        tmp_color = 0
        for j in range(0, 3):
            tmp_color += colorlist[i][j]
        tmp_key = colorlist[i]
        total_color_dict[tmp_key] = tmp_color
    sorted_total_color = sorted(total_color_dict.items(), key=operator.itemgetter(1))
    #print (type(sorted_total_color))
    sorted_color = []
    print ("sorted total color: ", sorted_total_color)
    #for keys in sorted_total_color.keys():
    #    sorted_color.append(keys)
    #print ("sorted: ", sorted_color)

    dist_dict = {}
    for i in range(0, len(colorlist)-1):
        dist = 0
        for j in range(0, 3):
            dist += (colorlist[i][j] - colorlist[i+1][j])**2
        tmp_key = colorlist[i]
        dist_dict[tmp_key] = dist

    sorted_dist = sorted(dist_dict.items(), key=operator.itemgetter(1))
    print ("sorted dist: ", sorted_dist)

        

if __name__ == "__main__":
    ClearALL()
    filename = "1_2.png"
    count, r, g, b, color = colornumber(filename)
    r_type, g_type, b_type = Kdetermine(count, r, g, b, color)
    GenTypeImg(b_type, "b_type")
    color_list = CompareSimilarImg()
    SortColor(color_list)
    #print ("color list: ", color_list)
    #distance_list = CompareDistance(color_list)
    #print ("distance list: ", distance_list)
    #new_color_list = SimpleColor(color_list)