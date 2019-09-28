# painting.py

import os
import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt
from preprocess import Kmeans
from monitor import Monitor
import tkinter as tk
import csv
from utils import BlankImg


class Painting():
    def __init__(self, K, shape):
        #self.radius = 3
        self.K = K
        self.size = shape
        self.count = 0
        self.fixcount = 0
        self.brush_size = 3
        self.img = np.zeros((self.size))
        for i in range(0, self.size[0]):
            for j in range(0, self.size[1]):
                self.img[i, j, 0] = self.img[i, j, 1] = self.img[i, j, 2] = 255

    def Painting(self):
        img = BlankImg(self.size)
        self.color_list = []
        for i in range(0, self.K):
            filename = "./points/" + str(i) + "_point.csv"
            with open(filename, newline='') as csvfile:
                rows = csv.reader(csvfile)
                for row in rows:
                    #print(row)
                    if (len(row) != 2):
                        r, g, b = int(row[3]), int(row[4]), int(row[5])
                        self.color_list.append((r, g, b))
                        print (r, g, b)
                    else:
                        x = int(row[0])
                        y = int(row[1])
                        for a in range(x-self.brush_size, x+self.brush_size):
                            for b in range(y-self.brush_size, y+self.brush_size):
                                if (a >= 0 and a <= self.size[0]-1):
                                    if (b >= 0 and b <= self.size[1]-1):
                                        img[a, b, 0] = r
                                        img[a ,b ,1] = g
                                        img[a ,b, 2] = b
                save_name = "./painting/" + str(i) + ".png"
                cv.imwrite(save_name, img)
                words = "finished " + str(i)
                print (words)
        return (self.color_list)

    def DectectImg(self, targetname, comparename):
        target_img = cv.imread(targetname)
        compare_img = cv.imread(comparename)
        different_img = BlankImg(self.size)
        for x in range(0, self.size[0]):
            for y in range(0, self.size[1]):
                if (int(target_img[x, y, 0]) != int(compare_img[x, y, 0])):
                    different_img[x, y, 0] = target_img[x, y, 0]
                    different_img[x, y, 1] = target_img[x, y, 1]
                    different_img[x, y, 2] = target_img[x, y, 2]
                else:
                    if (int(target_img[x, y, 1]) != int(compare_img[x, y, 1])):
                        different_img[x, y, 0] = target_img[x, y, 0]
                        different_img[x, y, 1] = target_img[x, y, 1]
                        different_img[x, y, 2] = target_img[x, y, 2]
                    else:
                        if (int(target_img[x, y, 2]) != int(compare_img[x, y, 2])):
                            different_img[x, y, 0] = target_img[x, y, 0]
                            different_img[x, y, 1] = target_img[x, y, 1]
                            different_img[x, y, 2] = target_img[x, y, 2]
        save_name = "./difference/" + str(self.count) + ".png"
        cv.imwrite(save_name, different_img)
        self.count += 1

    def Fixing(self, filename):
        img = cv.imread(filename)
        for i in range(0, len(self.color_list)):
            save_name = "./fixpoint/" + str(i) + ".csv"
            with open(save_name, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([self.color_list[i][0], self.color_list[i][1], self.color_list[i][2]])
                for x in range(0, self.size[0]):
                    for y in range(0, self.size[1]):
                        if (int(img[x, y, 0]) == int(self.color_list[i][0])):
                            if (int(img[x, y, 1]) == int(self.color_list[i][1])):
                                if (int(img[x, y, 2]) == int(self.color_list[i][2])):
                                    writer.writerow([x, y])






if __name__ == "__main__":
    K = 298
    filename = "K_298_1_2.png"
    img = cv.imread(filename)
    size = img.shape
    new = Painting(K, size)
    #filename = "./points/0_line.csv"
    color_list = new.Painting()
    comparename = "./painting/297.png"
    new.DectectImg(filename, comparename)
    new.Fixing("./difference/0.png")
    print ("finished.")
