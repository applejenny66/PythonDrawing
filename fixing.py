# fixing.py

import os
import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt
from preprocess import SimulateImg
from draw import DrawImg
import tkinter as tk
import csv

class Fixing():
    def __init__(self, name, K):
        self.name = name
        self.img = cv.imread(name)
        self.K = K
        self.size = self.img.shape
        self.brush_size = 5 # set as 5 (initial)
        self.color_sequence = []
        self.tmp_img = np.zeros((self.size[0], self.size[1], 1))
        for i in range(0, self.size[0]):
            for j in range(0, self.size[1]):
                self.tmp_img[i, j, 0] = self.tmp_img[i, j, 1] = self.tmp_img[i, j, 2] = -1
    
    def DrawStep(self, K):
        r = []
        g = []
        b = []
        common_name = "./sequence/"
        for i in range(0, self.K):
            filename = common_name + str(i) + ".png"
            print ("filename: ", filename)
            tmp_color = cv.imread(filename)[10, 10]
            tmp_r, tmp_g, tmp_b = tmp_color[0], tmp_color[1], tmp_color[2]
            r.append(tmp_r)
            g.append(tmp_g)
            b.append(tmp_b)
            self.color_sequence.append(tmp_color) #(0, 1, 2, 3, 4, 5)
        for x in range(0, self.size[0]):
            for y in range(0, self.size[1]):
                color_index = -1
                if (self.img[x, y, 0] in r):
                    r_index = r.index(self.img[x, y, 0])
                    if (self.img[x, y, 1] in g):
                        g_index = g.index(self.img[x, y, 1])
                        if (int(r_index) == int(g_index)):
                            if (self.img[x, y, 2] in b):
                                b_index = b.index(self.img[x, y, 2])
                                if (int(g_index) == int(b_index)):
                                    color_index = int(g_index)
                        else:
                            tmp_index = max(r_index, g_index)
                            if (self.img[x, y, 2] in b):
                                b_index = b.index(self.img[x, y, 2])
                                if (int(tmp_index) == int(b_index)):
                                    color_index = int(b_index) #(0, 1, 2, 3, 4, 5)
                if (color_index != (-1)):
                    self.tmp_img[x, y, 0] = color_index
        
                            



                


    def brushsize(self):

        pass
    
    def printf(self):
        print ("size: ", self.size)
        print ("color sequence: ", self.color_sequence)


if __name__ == "__main__":
    K = 6
    new = Fixing("./fixpoint/0_fix.png")
    new.DrawStep()
    new.printf()
