# draw.py

import os
import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt
import csv
from preprocess import SimulateImg


class DrawImg():
    def __init__(self, name, K, sequence_color, pa):
        self.name = name
        self.img = cv.imread(name)
        self.K = K
        self.size = self.img.shape
        self.sequence_color = sequence_color
        self.pa = pa
        self.total_area = self.size[0] * self.size[1]
        self.threshold = self.pa * self.total_area
        self.line = False
        self.color_line = [] # r, g, b color
        self.color_point = [] # r, g, b color
    
    def CheckLine(self):
        print ("threshold: ", self.threshold)
        for i in range(0, self.K):
            count = 0
            for x in range(0, self.size[0]):
                for y in range(0, self.size[1]):
                    if (int(self.img[x, y, 0]) == int(self.sequence_color[i][0]) and \
                        int(self.img[x, y, 1]) == int(self.sequence_color[i][1]) and \
                        int(self.img[x, y, 2]) == int(self.sequence_color[i][2])): 
                        count += 1
            print ("color: ", self.sequence_color[i])
            print ("count: ", count)
            print ("percentage of total area: ", count/self.total_area)
            
            if (count >= self.threshold):
                self.color_line.append(self.sequence_color[i])
        if (self.color_line != []):
            self.line = True
            #return (color_line)
        else:
            print ("There's no area over threshold.")

    def DrawLine(self):
        if (self.line == False):
            pass
        else:
            color_number = len(self.color_line)
            print ("line's color number: ", color_number)
            Points = np.zeros((self.size[0], self.size[1], color_number))
            for i in range(0, color_number):
                count = 0
                for x in range(0, self.size[0]):
                    for y in range(0, self.size[1]):
                        if (self.img[x, y, 0] == self.color_line[i][0] and \
                            self.img[x, y, 1] == self.color_line[i][1] and \
                            self.img[x, y, 2] == self.color_line[i][2]):
                            Points[x, y, i] = 1
                            count += 1
                words = str(i) + " lines number:"
                print (words, count)
            return (Points)

    def DrawPoints(self): 
        ############################################ problems
        ############################## only color cluster 3 (out of 4) with points 50. others are 0.

        self.color_point = [color for color in self.sequence_color if color not in self.color_line]
        if (self.color_point == []):
            print ("there's no single point.")
        else:
            color_number = len(self.color_point)
            print ("point's color number: ", color_number)
            Points = np.zeros((self.size[0], self.size[1], color_number))
            for i in range(0, color_number):
                count = 0
                for x in range(0, self.size[0]):
                    for y in range(0, self.size[1]):
                        if (int(self.img[x, y, 0]) == int(self.color_point[i][0]) and \
                            int(self.img[x, y, 1]) == int(self.color_point[i][1]) and \
                            int(self.img[x, y, 2]) == int(self.color_point[i][2])):
                            Points[x, y, i] = 1
                            count += 1
                words = str(i) + " points number:"
                print (words, count)
            return (Points)

    def GenSequence(self, line_points, single_points):
        if (self.color_line == []):
            pass
        else:
            total_color_number = len(self.color_line)
            for i in range(0, total_color_number):
                filename = './points/' + str(i) + '_line.csv'
                with open (filename, 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([self.color_line[i][0], self.color_line[i][1], self.color_line[i][2]])
                    for x in range(0, self.size[0]):
                        tmp_y = []
                        for y in range(0, self.size[1]):
                            if (line_points[x, y, i] == 1):
                                tmp_x = x
                                tmp_y.append(y)
                        if (len(tmp_y) == 0):
                            pass
                        elif (len(tmp_y) == 1):
                            writer.writerow([tmp_x, tmp_y[0]])
                        else:
                            min_y = min(tmp_y)
                            max_y = max(tmp_y)
                            writer.writerow([tmp_x, min_y])
                            writer.writerow([tmp_x, max_y])
        
        if (self.color_point == []):
            pass
        else:
            total_color_number = len(self.color_point)
            for i in range(0, total_color_number):
                filename = './points/' + str(i) + '_point.csv'
                with open (filename, 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([self.color_point[i][0], self.color_point[i][1], self.color_point[i][2]])
                    for x in range(0, self.size[0]):
                        for y in range(0, self.size[1]):
                            if (single_points[x, y, i] == 1):
                                writer.writerow([x, y])




def readcsv(filename):
    with open (filename, 'r', newline='') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            print (row)

            



if __name__ == "__main__":
    K = 6
    preprocess = SimulateImg("sunflower.jpg", K)
    #preprocess.printf()
    preprocess.Kmeans() # get the k means img
    preprocess.ColorSequence()
    preprocess.Monitor()
    preprocess.printf()
    drawpoints = DrawImg(preprocess.save_name, K, preprocess.sequence_color, 0.01)
    drawpoints = DrawImg("K_6_sunflower.jpg", K, preprocess.sequence_color, 0.01)
    drawpoints.CheckLine()
    try:
        line_point = drawpoints.DrawLine()
    except:
        pass
    try:
        single_point = drawpoints.DrawPoints()
    except:
        pass
    drawpoints.GenSequence(line_point, single_point)
    readcsv("./points/3_point.csv")