# painting.py

import os
import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt
from preprocess import SimulateImg
from draw import DrawImg
import tkinter as tk
import csv

class Painting():
    def __init__(self, K, shape):
        #self.radius = 5
        self.K = K
        self.size = shape
        self.count = 0
        self.fixcount = 0
        self.brush_size = 5
        self.img = np.zeros((self.size))
        for i in range(0, self.size[0]):
            for j in range(0, self.size[1]):
                self.img[i, j, 0] = self.img[i, j, 1] = self.img[i, j, 2] = 255

    def readfile_line(self, filename):
        self.brush_size = 10
        with open (filename, 'r', newline='') as csvfile:
            rows = csv.reader(csvfile)
            #count = 0
            for row in rows:
                if (len(row) == 6):
                    #print (row)
                    r, g, b = int(row[3]), int(row[4]), int(row[5])
                    print (r, g, b)
                
                else:
                    if (len(row) == 2):
                        x = int(row[0])
                        y = int(row[1])
                        for i in range(x-10, x+10):
                            if (i >= 0 and i < self.size[0]):
                                self.img[i, y, 0] = r
                                self.img[i, y, 1] = g
                                self.img[i, y, 2] = b
                    else:
                        x = int(row[0])
                        start_y = int(row[1])
                        end_y = int(row[2])
                        for i in range(x-self.brush_size, x+self.brush_size):
                            if (i >= 0 and i < self.size[0]):
                                for j in range(start_y, end_y):
                                    self.img[i, j, 0] = r
                                    self.img[i, j, 1] = g
                                    self.img[i, j, 2] = b

        save_name = "./painting/" + str(self.count) + "_paint.png"
        cv.imwrite(save_name, self.img)
        self.count += 1
        print ("save name: ", save_name)
        return (self.count)
    
    def readfile_points(self, filename):
        self.brush_size = 3
        with open (filename, 'r', newline='') as csvfile:
            rows = csv.reader(csvfile)
            #count = 0
            for row in rows:
                if (len(row) == 6):
                    r, g, b = int(row[3]), int(row[4]), int(row[5])
                    print (r, g, b)
                
                else:
                    if (len(row) == 2):
                        x = int(row[0])
                        y = int(row[1])
                        for i in range(x-self.brush_size, x+self.brush_size):
                            if (i >= 0 and i < self.size[0]):
                                for j in range(y-self.brush_size, y+self.brush_size):
                                    if (j >= 0 and j < self.size[1]):
                                        self.img[i, j, 0] = r
                                        self.img[i, j, 1] = g
                                        self.img[i, j, 2] = b
                    else:
                        pass

        save_name = "./painting/" + str(self.count) + "_paint.png"
        cv.imwrite(save_name, self.img)
        self.count += 1
        print ("save name: ", save_name)
        return (self.count)
    
    def DectectImg(self, targetname, comparedname):
        targetimg = cv.imread(targetname)
        comparedimg = cv.imread(comparedname)
        fiximg = np.zeros((self.size))
        
        for x in range(0, self.size[0]):
            for y in range(0, self.size[1]):
                if (targetimg[x, y, 0] == comparedimg[x, y, 0] and \
                    targetimg[x, y, 1] == comparedimg[x, y, 1] and \
                    targetimg[x, y, 2] == comparedimg[x, y, 2]):
                    fiximg[x, y, 0] = fiximg[x, y, 1] = fiximg[x, y, 2] = 255
                else:
                    fiximg[x, y, 0] = targetimg[x, y, 0]
                    fiximg[x, y, 1] = targetimg[x, y, 1]
                    fiximg[x, y, 2] = targetimg[x, y, 2]

        save_name = "./fixpoint/" + str(self.fixcount) + "_fix.png"
        cv.imwrite(save_name, fiximg)
        print ("save name: ", save_name)
        self.fixcount += 1
        return (save_name)


if __name__ == "__main__":
    new = Painting(6, (399, 600, 3))
    filename = "./points/0_line.csv"
    new.readfile_line(filename)
    for i in range(0, 5):
        filename = "./points/" + str(i) + "_point.csv"
        new.readfile_points(filename)
    new.DectectImg("K_6_sunflower.png", "./painting/5_paint.png")