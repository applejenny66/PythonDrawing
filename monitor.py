# draw.py

import os
import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt
import csv
from preprocess import Kmeans


class Monitor():
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
    
    #def LoadColor(self):
        

    def CheckLine(self):
        print ("threshold: ", self.threshold)
        tmp_count_array = np.zeros((self.K))
        for x in range(0, self.size[0]):
            for y in range(0, self.size[1]):
                tmp_point_color = tuple(self.img[x, y])
                #print (tmp_point_color)
                #print (type(tmp_point_color))
                if (tmp_point_color in self.sequence_color):
                    tmp_index = self.sequence_color.index(tmp_point_color)
                    tmp_count_array[tmp_index] += 1


                
        print ("finished.")
        for x in range(0, self.K):
            if (tmp_count_array[x] != 0):
                print (tmp_count_array[x])
                
            #print ("percentage of total area: ", count/self.total_area)
            
        #if (count >= self.threshold):
        #    self.color_line.append(self.sequence_color[i])
        #if (self.color_line != []):
        #    self.line = True
            #return (color_line)
        #else:
        #    print ("There's no area over threshold.")
        #print ("count: ", count)

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
            total_line_number = 0
        else:
            total_line_number = len(self.color_line)
            for i in range(0, total_line_number):
                filename = './points/' + str(i) + '_line.csv'
                with open (filename, 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(["r", "g", "b", self.color_line[i][0], self.color_line[i][1], self.color_line[i][2]])
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
                            writer.writerow([tmp_x, min_y, max_y])
                            #writer.writerow([tmp_x, max_y])
        
        if (self.color_point == []):
            total_point_number = 0
        else:
            total_point_number = len(self.color_point)
            for i in range(0, total_point_number):
                filename = './points/' + str(i) + '_point.csv'
                with open (filename, 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(["r", "g", "b", self.color_point[i][0], self.color_point[i][1], self.color_point[i][2]])
                    for x in range(0, self.size[0]):
                        for y in range(0, self.size[1]):
                            if (single_points[x, y, i] == 1):
                                writer.writerow([x, y])
        return (total_line_number, total_point_number)

    """
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
    """




if __name__ == "__main__":
    K = 298
    preprocess = Kmeans("1_2.png", K)
    preprocess.Kimg() # get the k means img
    sequence_color = preprocess.ColorSequence()
    print ("sequence color length: ", len(sequence_color))
    #preprocess.printf()
    #drawpoints = Monitor(preprocess.save_name, K, preprocess.sequence_color, 0.4)
    simulation = Monitor("K_298_1_2.png", K, sequence_color, 0.4)
    simulation.CheckLine()
    try:
        line_point = drawpoints.DrawLine()
    except:
        print ("there's error for line point.")
    try:
        single_point = drawpoints.DrawPoints()
    except:
        print ("there's error for single point.")
    simulation.GenSequence(line_point, single_point)
    #readcsv("./points/3_point.csv")