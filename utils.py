# utils.py
import os
import shutil

def jpgtopng(filename, savename):
    from PIL import Image
    im = Image.open(filename) # 'sunflower.jpg'
    im.save(savename) # 'sunflower.png'

def readcsv(filename):
    import csv
    with open (filename, 'r', newline='') as csvfile:
        rows = csv.reader(csvfile)
        count = 0

        for row in rows:
            if (count < 5):
                print (row)
            else:
                break
            count += 1

def ClearALL():
    dir_list = ['./monitor_fix', './sequence', './color_result', './fixpoint', './monitor_pic', \
                './painting', './points', ]
    for dir_name in dir_list:
        shutil.rmtree(dir_name)  
        os.mkdir(dir_name)

if __name__ == "__main__":
    count = 0
    for name in os.listdir("./sequence/"):
        filename = "./sequence/" + name
        save_name = filename.replace('jpg', 'png')
        jpgtopng(filename, save_name)
        count += 1