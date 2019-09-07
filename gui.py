# gui.py


import os
import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt

from preprocess import SimulateImg
from draw import DrawImg

import tkinter as tk

root = tk.Tk()
root.title('simulate image')
root.resizable(False, False)    #固定窗口大小
windowWidth = 800               #获得当前窗口宽
windowHeight = 500              #获得当前窗口高
screenWidth,screenHeight = root.maxsize()     #获得屏幕宽和高
geometryParam = '%dx%d+%d+%d'%(windowWidth, windowHeight, (screenWidth-windowWidth)/2, (screenHeight - windowHeight)/2)
root.geometry(geometryParam)    #设置窗口大小及偏移坐标
root.wm_attributes('-topmost',1)#窗口置顶
 
#label文本
label_text = tk.Label(root, text = 'simulating process')
label_text.pack()
 
#label图片
img = tk.PhotoImage(file = 'sunflower.png')
label_img = tk.Label(root, image = img)
label_img.pack()
"""

 
#带图button，image
button_img_gif = tk.PhotoImage(file = 'button_gif.gif')
button_img = tk.Button(root, image = button_img_gif, text = '带图按钮')
button_img.pack()
 
#带图button，bitmap
button_bitmap = tk.Button(root, bitmap = 'error', text = '带图按钮')
button_bitmap.pack()
"""
root.mainloop()





