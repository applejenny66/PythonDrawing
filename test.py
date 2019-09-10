
import shutil
import os



def ClearALL():
    dir_list = ['./monitor_fix', './sequence', './color_result', './fixpoint', './monitor_pic', \
                './painting', './points', ]
    for dir_name in dir_list:
        shutil.rmtree(dir_name)  
        os.mkdir(dir_name)
    