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
from utils import ClearALL, colornumber
import time
from gui import GUI
from simplifycolor import *

def step0(filename):
    ClearALL()
    #filename = "1_2.png"
    count, r, g, b, color = colornumber(filename)
    r_type, g_type, b_type = TypeClassify(count, r, g, b, color)
    r_sum, g_sum, b_sum = SortSumColor(r_type), SortSumColor(g_type), SortSumColor(b_type)
    r_tidy, g_tidy, b_tidy = RemoveRedundant(r_sum), RemoveRedundant(g_sum), RemoveRedundant(b_sum)
    r_distance, g_distance, b_distance = CalculateDistance(r_tidy)[0], CalculateDistance(g_tidy)[0], CalculateDistance(b_tidy)[0]
    simple_r, similar_r = SimplifyColor(r_distance)
    simple_g, similar_g = SimplifyColor(g_distance)
    simple_b, similar_b = SimplifyColor(b_distance)
    tidy_simple_r, tidy_simple_g, tidy_simple_b = RemoveRedundant(simple_r), RemoveRedundant(simple_g), RemoveRedundant(simple_b)
    GenTypeImg(tidy_simple_r, "b_type"), GenTypeImg(tidy_simple_g, "g_type"), GenTypeImg(tidy_simple_b, "r_type")
    K = Kdecided(simple_r, simple_g, simple_b)
    print ("K: ", K)
    print ("finished step 0.")
    return (K)


def step1(filename, Kfilename, K, shape):

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
    line_count = 0
    count = 0
    for i in range(0, line_file_number):
        line_file_name = "./points/" + str(i) + "_line.csv"
        line_count = painting.readfile_line(line_file_name)
    for j in range(0, point_file_number):
        point_file_name = "./points/" + str(j) + "_point.csv"
        count = painting.readfile_points(point_file_name)
    total_count = count - line_count ##### total_count 
    file_count = 0
    for filename in os.listdir("./painting/"):
        file_count += 1
    print ("file count: ", file_count)
    final_painting_name = "./painting/" + str(file_count-1) + "_paint.png"

    print ("final_painting_name: ", final_painting_name)

    filename = painting.DectectImg(Kfilename, final_painting_name)
    fixing = Fixing(filename, K)
    fixing.DrawStep()
    fixing.Simulatefix()
    fixing.printf()
    fixing.Painting(final_painting_name)

if __name__ == "__main__":
    filename = "2_2.png"
    K = step0(filename)
    count, r, g, b, color = colornumber(filename)
    print ("count: ", count)
    Kfilename = "K_" + str(K) + "_" + filename
    img = cv.imread(filename)
    shape = img.shape
    
    #print ("color: ", color)
    #fix_time = 0
    
    step1(filename, Kfilename, K, shape)
    #gui = GUI()
    #count = 0
    #gui.setting()
    

