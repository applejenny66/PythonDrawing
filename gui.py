# gui.py

import os
import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt
from preprocess import SimulateImg
from draw import DrawImg
import tkinter as tk

class GUI():
    def __init__(self):
        self.window = tk.Tk()
        self.count = 0
        self.name = "./monitor_pic/" + str(self.count) + ".png"
        """
        img = tk.PhotoImage(file = filename)
        label_img = tk.Label(self.window, image = img)
        label_img.pack()
        self.window.mainloop()
        """
    
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
        img = tk.PhotoImage(file = self.name)
        label_img = tk.Label(self.window, image = img)
        label_img.pack()

        #frame1 = tk.Frame(illustration)
        button_previous = tk.Button(self.window, text="previous", command = self.clear).pack() # .pack(side="left")
        button_next = tk.Button(self.window, text="next", command = self.function_next).pack()
        #frame2 = tk.Frame(illustration)
        #frame3 = tk.Frame(illustration)
        #button_next = tk.Button(illustration, text="next", command=callback)
        #button_next.pack()
        self.window.mainloop()

    def function_next(self):
        # label scripts
        
        print ("ok")
        
        print ("count: ", self.count)
        self.count += 1
        
        label_text = tk.Label(self.window, text = 'simulating process')
        label_text.pack()
        # label image
        filename = "./monitor_pic/" + str(self.count) + ".png"
        print ("filename: ", filename)
        
        img = tk.PhotoImage(file = filename)
        label_img = tk.Label(self.window, image = img)
        label_img.pack()
        self.window.mainloop()
        print ("finished.")
        
    def clear(self):
        list = self.window.grid_slaves()
        for l in list:
            l.destroy()


if __name__ == "__main__":
    K = 6
    gui = GUI()
    
    count = 0
    #filename = "./monitor_pic/" + str(count) + ".png"
    gui.setting()
    #gui.function_next(count)



