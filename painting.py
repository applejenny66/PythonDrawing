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
        self.radius = 5
        self.K = K
        self.size = shape

    def readfile(self, filename):
        img = np.zeros((self.size[0], self.size[1], 3))
        with open (filename, 'r', newline='') as csvfile:
            rows = csv.reader(csvfile)
            count = 0
            for row in rows:
                if (len(row) == 3):
                    r, g, b = row[0], row[1], row[2]
                """
                else:
                    img[row[0], row[1], 0] = r
                    img[row[0], row[1], 1] = g
                    img[row[0], row[1], 2] = b
                """
                print (r, g, b)
                
            


if __name__ == "__main__":
    new = Painting(6, (399, 600, 3))
    filename = "./points/0_line.csv"
    new.readfile(filename)