# gui.py

import os
import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt
from preprocess import Kmeans
from monitor import Monitor
import tkinter as tk

class GUI():
    def __init__(self, dir, tail):
        self.window = tk.Tk()
        self.count = 0
        self.dir = dir
        self.tail = tail
        self.name = self.dir + str(self.count) + str(self.tail)
        self.img = tk.PhotoImage(file = self.name)
        self.label_img = tk.Label(self.window, image = self.img)
    
    def setting(self):
        self.window.title('simulate image')
        self.window.resizable(False, False)    # fix size of window
        windowWidth = 800               # width of window
        windowHeight = 500              # height of window
        screenWidth,screenHeight = self.window.maxsize()     # width and height of screen
        geometryParam = '%dx%d+%d+%d'%(windowWidth, windowHeight, (screenWidth-windowWidth)/2, (screenHeight - windowHeight)/2)
        self.window.geometry(geometryParam)     # set size and cordinate
        self.window.wm_attributes('-topmost',1) # window to the top
        
        # label scripts
        label_text = tk.Label(self.window, text = 'simulating process')
        label_text.pack()
        
        # label image
        #img = tk.PhotoImage(file = self.name)
        #label_img = tk.Label(self.window, image = self.img)
        button_previous = tk.Button(self.window, text="previous", command = self.function_previous).pack() # .pack(side="left")
        button_next = tk.Button(self.window, text="next", command = self.function_next).pack()
        self.label_img.pack()

        #frame1 = tk.Frame(illustration)
        
        #frame2 = tk.Frame(illustration)
        #frame3 = tk.Frame(illustration)
        #button_next = tk.Button(illustration, text="next", command=callback)
        #button_next.pack()
        self.window.mainloop()

    def function_next(self):
        # label scripts
        self.label_img.destroy()
        #print ("ok")
        print ("count: ", self.count)
        self.count += 1
        # label image
        filename = self.dir + str(self.count) + str(self.tail)
        print ("filename: ", filename)
        
        self.img = tk.PhotoImage(file = filename)
        self.label_img = tk.Label(self.window, image = self.img)
        self.label_img.pack()
        self.window.mainloop()

    def function_previous(self):
        # label scripts
        self.label_img.destroy()
        print ("count: ", self.count)
        self.count -= 1
        # label image
        filename = self.dir + str(self.count) + str(self.tail)
        print ("filename: ", filename)
        
        self.img = tk.PhotoImage(file = filename)
        self.label_img = tk.Label(self.window, image = self.img)
        self.label_img.pack()
        self.window.mainloop()
        


if __name__ == "__main__":
    K = 6
    dir_name = "./painting/"
    tail_name = "_paint.png"
    gui = GUI(dir_name, tail_name)
    gui.setting()



