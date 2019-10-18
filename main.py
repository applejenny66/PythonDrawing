# main.py

import os
import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt
import csv

from preprocess import Kmeans
from monitor import Monitor
from painting import Painting
from fixing import Fixing
from utils import ClearALL, colornumber, RemoveRedundant
import time
from gui import GUI
from Kdecide import *

def step0(filename):
    #Kdecide.py
    ClearALL()
    filename = "1_2.png"
    count, r, g, b, color = colornumber(filename)
    r_type, g_type, b_type = TypeClassify(count, r, g, b, color)
    r_sum, g_sum, b_sum = SortSumColor(r_type), SortSumColor(g_type), SortSumColor(b_type)
    r_tidy, g_tidy, b_tidy = RemoveRedundant(r_sum), RemoveRedundant(g_sum), RemoveRedundant(b_sum)
    r_distance, g_distance, b_distance = CalculateDistance(r_tidy), CalculateDistance(g_tidy), CalculateDistance(b_tidy)
    #print (r_distance)
    simple_r = SimplifyColor(r_distance)
    simple_g = SimplifyColor(g_distance)
    simple_b = SimplifyColor(b_distance)
    tidy_simple_r, tidy_simple_g, tidy_simple_b = RemoveRedundant(simple_r), RemoveRedundant(simple_g), RemoveRedundant(simple_b)
    #GenTypeImg(tidy_simple_r, "b_type"), GenTypeImg(tidy_simple_g, "g_type"), GenTypeImg(tidy_simple_b, "r_type")
    print ("r color: ", tidy_simple_r)
    print ("g color: ", tidy_simple_g)
    print ("b color: ", tidy_simple_b)
    K = Kdecided(simple_r, simple_g, simple_b)
    print ("K: ", K)
    printf()
    return (K)
    


def step1(filename, Kfilename, K, shape):
    #preprocess.py
    Kprocess = Kmeans(filename, K)
    Kprocess.Kimg() # get the k means img
    print ("K means img generated.")
    sequence_color = Kprocess.ColorSequence()
    print ("sequence color: ", sequence_color)
    print ("length of sequence color: ", len(sequence_color))

    #count, r, g, b, color = colornumber(Kfilename) 
    # has a bug -> the number of color is different to the k of k means
    #print ("count of total color: ", count)
    #Kprocess.ColorSequence()
    #Kprocess.Monitor()
    print ("simulated img generated.")
    time.sleep(0.5)
    #monitor.py
    sorted_sequence_color = Kprocess.SortColor()
    sorted_sequence_color = RemoveRedundant(sorted_sequence_color)
    monit_name = "K_" + str(K) + "_" + filename #"K_298_1_2.png"
    print ("monit_name: ", monit_name)
    simulation = Monitor(monit_name, K, sorted_sequence_color, 0.4)
    simulation.GenPoints()
    simulation.SimulatedImg()
    paint = Painting(K, shape)
    color_list = paint.Painting()
    comparename = "./painting/297.png"
    paint.DectectImg(monit_name, comparename)
    paint.Fixing("./difference/0.png")
    print ("finished.")
    time.sleep(0.5)
    fix = Fixing("./painting/297.png", K)
    fix.DrawStep()
    fix.Simulatefix()
    fix.printf()
    fix.Painting("./painting/297.png")

if __name__ == "__main__":
    filename = "1_2.png"
    img = cv.imread(filename)
    shape = img.shape
    K = step0(filename)
    Kfilename = "K_" + str(K) + "_" + filename
    print ("K means name: ", Kfilename)
    
    step1(filename, Kfilename, K, shape)
    #gui = GUI()
    #count = 0
    #gui.setting()
    

