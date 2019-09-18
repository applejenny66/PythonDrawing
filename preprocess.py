# preprocess.py
# sunflower.png

import os
import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt
from utils import GenColorImg


class Kmeans():
    def __init__(self, name, K):
        self.name = name
        self.K = K
        self.img = cv.imread(name)
        self.size = self.img.shape
        self.sequence_color = []

    def Kimg(self):
        # gen k means img (res2) and save img
        Z = self.img.reshape((-1,3))
        Z = np.float32(Z)
        # define criteria, number of clusters(K) and apply kmeans()
        criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        ret,label,center=cv.kmeans(Z,self.K,None,criteria,10,cv.KMEANS_RANDOM_CENTERS)
        center = np.uint8(center)
        res = center[label.flatten()]
        res2 = res.reshape((self.size))
        save_name = "K_" + str(self.K) + "_" + self.name
        self.save_name = save_name
        cv.imwrite(save_name, res2)
        self.K_img = res2
        print ("K img generated.")
        #print (self.K_img.shape)

    def ColorSequence(self):  # gen coloring sequence -> light to deep 
        # save each sequence color
        color_r = []
        color_g = []
        color_b = []
        color = []
        color_total = []
        #save k number of color in k means img
        for x in range(0, self.size[0]):
            for y in range(0, self.size[1]):
                tmp_r = self.K_img[x, y, 0]
                tmp_g = self.K_img[x, y, 1]
                tmp_b = self.K_img[x, y, 2]
                if (tmp_r not in color_r):
                    color_r.append(tmp_r)
                    color_b.append(tmp_b)
                    color_g.append(tmp_g)
                    tmp_color = (tmp_r, tmp_g, tmp_b)
                    color.append(tmp_color)
                    tmp_total = int(tmp_r) + int(tmp_g) + int(tmp_b)
                    color_total.append(tmp_total)
                else:
                    if (tmp_g not in color_g):
                        color_r.append(tmp_r)
                        color_b.append(tmp_b)
                        color_g.append(tmp_g)
                        tmp_color = (tmp_r, tmp_g, tmp_b)
                        color.append(tmp_color)
                        tmp_total = int(tmp_r) + int(tmp_g) + int(tmp_b)
                        color_total.append(tmp_total)
                    else:
                        if (tmp_b not in color_b):
                            color_r.append(tmp_r)
                            color_b.append(tmp_b)
                            color_g.append(tmp_g)
                            tmp_color = (tmp_r, tmp_g, tmp_b)
                            color.append(tmp_color)
                            tmp_total = int(tmp_r) + int(tmp_g) + int(tmp_b)
                            color_total.append(tmp_total)
                        else:
                            tmp_color = (tmp_r, tmp_g, tmp_b)
                            if (tmp_color not in color):
                                color_r.append(tmp_r)
                                color_g.append(tmp_g)
                                color_b.append(tmp_b)
                                color.append(tmp_color)
                                tmp_total = int(tmp_r) + int(tmp_g) + int(tmp_b)
                                color_total.append(tmp_total)
        
        for i in range(0, self.K):
            lightest_color = max(color_total)
            lightest_index = color_total.index(lightest_color)
            r, g, b = color_r[lightest_index], color_g[lightest_index], color_b[lightest_index]
            self.sequence_color.append((r, g, b))
            save_color = [r, g, b]
            save_name = "./sequence/" + str(i) + ".png"
            GenColorImg(save_color, save_name)
            save_name = "./color_result/" + str(r) + "_" + str(g) + "_" + str(b) + ".png"
            GenColorImg(save_color, save_name)
            color_total.remove(lightest_color)
            color_r.remove(r)
            color_g.remove(g)
            color_b.remove(b)

        return (self.sequence_color)
        



    def printf(self):
        print ("img name: ", self.name)
        print ("K means: ", self.K)
        print ("shape: ", self.size)


if __name__ == "__main__":
    K = 298
    new = Kmeans("1_2.png", K)
    new.Kimg() # get the k means img
    sequence_color = new.ColorSequence()
    print ("sequence color: ", sequence_color)
    print ("length of sequence color: ", len(sequence_color))
    new.printf()
    



