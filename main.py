# main.py

import os
import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt
import csv

from preprocess import SimulateImg
from draw import DrawImg

def step1():
    Kprocess = SimulateImg(filename, K)
    #Kprocess.printf()
    Kprocess.Kmeans() # get the k means img
    Kprocess.ColorSequence()
    
    Kprocess.Monitor()
    Kprocess.printf()
    #drawpoints = DrawImg(preprocess.save_name, K, preprocess.sequence_color, 0.4)
    drawpoints = DrawImg("K_6_sunflower.png", K, Kprocess.sequence_color, 0.4)
    drawpoints.CheckLine()
    try:
        line_point = drawpoints.DrawLine()
        print ("trying")
    except:
        print ("no line points or there's problem for line points.")
    try:
        single_point = drawpoints.DrawPoints()
        print ("trying")
    except:
        print ("no single point or there's prpblem for single points.")
        
    drawpoints.GenSequence(line_point, single_point)
    #readcsv("./points/3_point.csv")
    

if __name__ == "__main__":
    filename = "sunflower.png"
    K = 6
    step1()
    
    

