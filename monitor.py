# draw.py

import os
import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt
import csv
from preprocess import Kmeans
from utils import RemoveRedundant, BlankImg

class Monitor():
    def __init__(self, name, K, sorted_sequence_color, pa):
        self.name = name
        self.img = cv.imread(self.name)
        self.K = K
        self.size = self.img.shape
        self.sequence_color = sorted_sequence_color
        self.pa = pa
        self.total_area = self.size[0] * self.size[1]
        self.threshold = self.pa * self.total_area
        self.line = False
        self.color_line = [] # r, g, b color
        self.color_point = [] # r, g, b color
    

    def GenPoints(self):
        point_array = np.zeros((self.size[0], self.size[1], 1))
        set_sequence_list = []
        for i in range(0, len(self.sequence_color)):
            tmp = set(self.sequence_color[i])
            set_sequence_list.append(tmp)
        count = 0
        for x in range(0, self.size[0]):
            for y in range(0, self.size[1]):
                #print ("x, y: ", x, y)
                tmp_color = set(self.img[x, y])
                print ("tmp color: ", tmp_color)
                #print (tmp_color)
                if (tmp_color in set_sequence_list):  ############################
                    tmp_index = set_sequence_list.index(tmp_color)
                    point_array[x, y, 0] = int(tmp_index)
                    #count += 1
                else:
                    point_array[x, y] = int(-1)
                    count += 1
        print ("count: ", count)
        print ("color number: ", count)   
        for i in range(0, self.K):
            filename = './points/' + str(i) + '_point.csv'
            with open (filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["r", "g", "b", self.sequence_color[i][0], self.sequence_color[i][1], self.sequence_color[i][2]])
                #count = 0
                for x in range(0, self.size[0]):
                    for y in range(0, self.size[1]):
                        if (int(point_array[x, y]) == int(i)):
                            writer.writerow([x, y])
                        elif (point_array[x, y] == -1):
                            pass
                            #count += 1
                            #print ("there's some error.")

    def SimulatedImg(self):
        img = BlankImg(self.size)
        for i in range(0, self.K):
            filename = './points/' + str(i) + '_point.csv'
            
            with open(filename, newline='') as csvfile:
                rows = csv.reader(csvfile)
                #tmp = rows[0]
                #print ("first row", tmp)
                for row in rows:
                    if (len(row) != 2):
                        r, g, b = int(row[3]), int(row[4]), int(row[5])
                    else:
                        x = int(row[0])
                        y = int(row[1])
                        img[x, y, 0] = r
                        img[x ,y ,1] = g
                        img[x ,y, 2] = b
                save_name = "./monitor_pic/" + str(i) + ".png"
                cv.imwrite(save_name, img)
                words = "finished " + str(i)
                print (words)
                     

    def showimg(self):
        print ("self.name: ", self.name)
        cv.imshow("1", self.img)
        cv.waitKey(0)


if __name__ == "__main__":
    K = 298
    preprocess = Kmeans("1_2.png", K)
    preprocess.Kimg() # get the k means img
    sequence_color = preprocess.ColorSequence()
    #print ("sequence color length: ", len(sequence_color))
    sorted_sequence_color = preprocess.SortColor()
    sorted_sequence_color = RemoveRedundant(sorted_sequence_color)
    simulation = Monitor("K_298_1_2.png", K, sorted_sequence_color, 0.4)
    #simulation.showimg()
    simulation.GenPoints()
    simulation.SimulatedImg()
