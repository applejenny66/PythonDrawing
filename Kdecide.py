# Kdecide.py

from utils import colornumber
import numpy as np
import cv2 as cv
from utils import ClearALL
import operator
from utils import RemoveRedundant

def TypeClassify(count, r, g, b, color):
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

def SortSumColor(colorlist):
    sum_list = []
    for i in range(0, len(colorlist)):
        tmp_dist = 0
        tmp_color = []
        tmp_total = []
        for j in range(0, 3):
            tmp_dist += (colorlist[i][j]**2)
            tmp_color.append(colorlist[i][j])
        tmp_total.append(tmp_color)
        tmp_total.append(tmp_dist)
        sum_list.append(tmp_total)
    sorted_sum_list = sorted(sum_list, key=operator.itemgetter(1)) # list
    return (sorted_sum_list)

def CalculateDistance(sortlist):
    distance_list = []
    for i in range(0, len(sortlist)-1):
        tmp_dist = 0
        tmp_color = []
        tmp_total = []
        for j in range(0, 3):
            tmp_dist += (sortlist[i][j] - sortlist[i+1][j])*(sortlist[i][j] - sortlist[i+1][j])
            tmp_color.append(sortlist[i][j])
        tmp_total.append(tmp_color)
        tmp_total.append(tmp_dist)
        distance_list.append(tmp_total)
    tmp_color = []
    tmp_total = []
    tmp_color.append(sortlist[len(sortlist)-1][0])
    tmp_color.append(sortlist[len(sortlist)-1][1])
    tmp_color.append(sortlist[len(sortlist)-1][2])
    tmp_total.append(tmp_color)
    tmp_total.append(tmp_dist)
    distance_list.append(tmp_total)
    #sorted_dictance_list = sorted(distance_list, key=operator.itemgetter(1)) # list
    #print ("sort distance dictionary: ", sorted_dictance_list)
    #return (distance_list, sorted_dictance_list)
    return (distance_list)


def SimplifyColor(colorlist):
    similar_color_list = []
    for i in range(0, len(colorlist)):
        if (colorlist[i][1] < 150):
            similar_color_list.append(colorlist[i])
    
    simple_color = [i for i in colorlist if i not in similar_color_list]
    #return (simple_color, similar_color_list)
    return (simple_color)

"""
def GenTypeImg(colorlist, colortype):
    length = len(colorlist)
    for i in range(0, len(colorlist)):
        img = np.zeros((100, 100, 3))
        color = colorlist[length - i - 1]
        for x in range(0, 100):
            for y in range(0, 100):
                img[x, y, 0] = color[0]
                img[x, y, 1] = color[1]
                img[x, y, 2] = color[2]
        save_name = "./all_color/" + str(colortype) + "/" + str(i) + ".png"
        cv.imwrite(save_name, img)
"""
def Kdecided(r, g, b):
    K = len(r) + len(g) + len(b)
    return (K)

def printf():
    try:
        print ("filename: ", filename)
    except:
        print ("unknow filename")
    try:
        #print ("similar r color number: ", len(similar_r))
        print ("simple r color number: ", len(simple_r))
    except:
        print ("unknown r color")
    try:
        #print ("similar g color number: ", len(similar_g))
        print ("simple g color number: ", len(simple_g))
    except:
        print ("unknown g color")
    try:
        #print ("similar b color number: ", len(similar_b))
        print ("simple b color number: ", len(simple_b))
    except:
        print ("unknown b color")
        
if __name__ == "__main__":
    ClearALL()
    filename = "1_2.png"
    count, r, g, b, color = colornumber(filename)
    r_type, g_type, b_type = TypeClassify(count, r, g, b, color)
    
    r_sum, g_sum, b_sum = SortSumColor(r_type), SortSumColor(g_type), SortSumColor(b_type)
    r_tidy, g_tidy, b_tidy = RemoveRedundant(r_sum), RemoveRedundant(g_sum), RemoveRedundant(b_sum)
    r_distance, g_distance, b_distance = CalculateDistance(r_tidy), CalculateDistance(g_tidy), CalculateDistance(b_tidy)
    #print (r_distance)
    simple_r = SimplifyColor(r_distance)
    simple_g = SimplifyColor(g_distance)
    simple_b = SimplifyColor(b_distance)
    tidy_simple_r, tidy_simple_g, tidy_simple_b = RemoveRedundant(simple_r), RemoveRedundant(simple_g), RemoveRedundant(simple_b)
    #GenTypeImg(tidy_simple_r, "b_type"), GenTypeImg(tidy_simple_g, "g_type"), GenTypeImg(tidy_simple_b, "r_type")
    print ("r color: ", tidy_simple_r)
    print ("g color: ", tidy_simple_g)
    print ("b color: ", tidy_simple_b)
    K = Kdecided(simple_r, simple_g, simple_b)
    print ("K: ", K)
    printf()

    