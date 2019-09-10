# main.py

import os
import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt
import csv

from preprocess import SimulateImg
from draw import DrawImg
from painting import Painting
from fixing import Fixing
from utils import ClearALL
import time

def step1(filename, Kfilename, K, shape):
    ClearALL()

    Kprocess = SimulateImg(filename, K)
    Kprocess.Kmeans() # get the k means img
    Kprocess.ColorSequence()
    Kprocess.Monitor()
    Kprocess.printf()

    drawpoints = DrawImg(Kfilename, K, Kprocess.sequence_color, 0.4)
    drawpoints.CheckLine()
    try:
        line_point = drawpoints.DrawLine()
        print ("trying line")
    except:
        print ("no line points or there's problem for line points.")
    try:
        single_point = drawpoints.DrawPoints()
        print ("trying point")
    except:
        print ("no single point or there's prpblem for single points.")
    line_file_number, point_file_number = drawpoints.GenSequence(line_point, single_point)

    painting = Painting(K, shape)
    for i in range(0, line_file_number):
        line_file_name = "./points/" + str(i) + "_line.csv"
        line_count = painting.readfile_line(line_file_name)
    for j in range(0, point_file_number):
        point_file_name = "./points/" + str(j) + "_point.csv"
        count = painting.readfile_points(point_file_name)
    total_count = count - line_count
    final_painting_name = "./painting/" + str(total_count) + "_paint.png"
    print ("final_painting_name: ", final_painting_name)

    filename = painting.DectectImg(Kfilename, final_painting_name)
    fixing = Fixing(filename, K)
    fixing.DrawStep()
    fixing.Simulatefix()
    fixing.printf()
    fixing.Painting(final_painting_name)

if __name__ == "__main__":
    K = 6
    filename = "sunflower.png"
    Kfilename = "K_" + str(K) + "_" + filename
    img = cv.imread(filename)
    shape = img.shape
    #fix_time = 0
    step1(filename, Kfilename, K, shape)
    
    

