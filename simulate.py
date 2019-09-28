# simulate.py
#################### problems
# sunflower.png

import os
import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt

class SimulateImg():
    def __init__(self, name, K): # k_means name
        self.name = name
        self.K = K
        self.K_img = cv.imread(name)
        self.size = self.K_img.shape
        self.sequence_color = []

    def ColorSequence(self):
        # gen coloring sequence -> light to deep 
        # save each sequence color
        color_r = []
        color_g = []
        color_b = []
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
                    tmp_total = int(tmp_r) + int(tmp_g) + int(tmp_b)
                    color_total.append(tmp_total)
                else:
                    if (tmp_g not in color_g):
                        color_r.append(tmp_r)
                        color_b.append(tmp_b)
                        color_g.append(tmp_g)
                        tmp_total = int(tmp_r) + int(tmp_g) + int(tmp_b)
                        color_total.append(tmp_total)
                    else:
                        if (tmp_b not in color_b):
                            color_r.append(tmp_r)
                            color_b.append(tmp_b)
                            color_g.append(tmp_g)
                            tmp_total = int(tmp_r) + int(tmp_g) + int(tmp_b)
                            color_total.append(tmp_total)
                        else:
                            tmp_r_index = color_r.index(tmp_r)
                            tmp_g_index = color_g.index(tmp_g)
                            tmp_b_index = color_b.index(tmp_b)
                            if (tmp_r_index == tmp_g_index == tmp_b_index):
                                pass
                            else:
                                color_r.append(tmp_r)
                                color_b.append(tmp_b)
                                color_g.append(tmp_g)
                                tmp_total = int(tmp_r) + int(tmp_g) + int(tmp_b)
                                color_total.append(tmp_total)
        #print ("r color: ", color_r)
        #print ("g color: ", color_g)
        #print ("b color: ", color_b)
        #print ("total color: ", color_total)
        
        for i in range(0, self.K):
            symbol_color = np.zeros((100, 100, 3))
            lightest_color = max(color_total)
            lightest_index = color_total.index(lightest_color)
            r, g, b = color_r[lightest_index], color_g[lightest_index], color_b[lightest_index]
            print (r, g, b)
            self.sequence_color.append((r, g, b))
            for m in range(0, 100):
                for n in range(0, 100):
                    symbol_color[m, n, 0] = r
                    symbol_color[m, n, 1] = g
                    symbol_color[m, n, 2] = b
            save_name = "./sequence/" + str(i) + ".png"
            cv.imwrite(save_name, symbol_color)
            del color_total[lightest_index]
            del color_r[lightest_index]
            del color_g[lightest_index]
            del color_b[lightest_index]
            #color_total.remove(lightest_color)
            #color_r.remove(r)
            #color_g.remove(g)
            #color_b.remove(b)
            #print (color_r)
            #print (color_g)
            #print (color_b)
        #self.sequence_color = sequence_color
        print ("sequence color: ", self.sequence_color)

    def Monitor(self):
        monitor_img = np.zeros(self.size)
        # black array to white
        for x in range(0, self.size[0]):
            for y in range(0, self.size[1]):
                monitor_img[x, y, 0] = monitor_img[x, y, 1] = monitor_img[x, y, 2] = 255
        # simulate coloring step by step
        for i in range(0, self.K):
            for j in range(0, self.size[0]):
                for k in range(0, self.size[1]):
                    #print (i, j, k)
                    if (self.K_img[j, k, 0] == self.sequence_color[i][0]):
                        if (self.K_img[j, k, 1] == self.sequence_color[i][1]):
                            if (self.K_img[j, k, 2] == self.sequence_color[i][2]):
                                monitor_img[j, k, 0] = self.sequence_color[i][0]
                                monitor_img[j, k, 1] = self.sequence_color[i][1]
                                monitor_img[j, k, 2] = self.sequence_color[i][2]
            save_name = "monitor_pic/" + str(i) + ".png"
            cv.imwrite(save_name, monitor_img)

    def printf(self):
        print ("img name: ", self.name)
        print ("K means: ", self.K)
        print ("shape: ", self.size)



if __name__ == "__main__":
    new = SimulateImg("K_6_sunflower.png", 6)
    new.printf()
    new.ColorSequence()
    new.Monitor()
    new.printf()
    




