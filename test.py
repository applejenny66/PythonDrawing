
import shutil
import os
import numpy as np
import operator   


class Kmeans():
    def __init__(self):
        self.sequence_color = []


    def SortColor(self):
        total_list = []
        for i in range(0, len(self.sequence_color)):
            tmp_total = 0
            tmp_color = []
            tmp_list = []
            for j in range(0, 3):
                tmp = (self.sequence_color[i][j] * self.sequence_color[i][j])
                print ("tmp: ", tmp)
                tmp_total += tmp
                tmp_color.append(self.sequence_color[i][j])
            tmp_list.append(tmp_color)
            tmp_list.append(tmp_total)
            total_list.append(tmp_list)
        sorted_sequence_color = sorted(total_list, key=operator.itemgetter(1))
        print ("sorted sequence color: ", sorted_sequence_color)
        return (sorted_sequence_color)


if __name__ == "__main__":
    new = Kmeans()
    new.sequence_color = [(118, 114, 59), (90, 100, 160), (164, 111, 210), (90, 109, 43), (56, 40, 147)]
    new.SortColor()
    print ("---", 90*90+109*109+43*43)