# tmp.py

    def Monitor(self):
        monitor_img = np.zeros(self.size)
        # black array to white
        for x in range(0, self.size[0]):
            for y in range(0, self.size[1]):
                monitor_img[x, y, 0] = monitor_img[x, y, 1] = monitor_img[x, y, 2] = 255
        # simulate coloring step by step
        for i in range(0, self.K):
            for j in range(0, self.size[0]):
                for k in range(0, self.size[1]):
                    #print (i, j, k)
                    if (self.K_img[j, k, 0] == self.sequence_color[i][0]):
                        if (self.K_img[j, k, 1] == self.sequence_color[i][1]):
                            if (self.K_img[j, k, 2] == self.sequence_color[i][2]):
                                monitor_img[j, k, 0] = self.sequence_color[i][0]
                                monitor_img[j, k, 1] = self.sequence_color[i][1]
                                monitor_img[j, k, 2] = self.sequence_color[i][2]
            save_name = "monitor_pic/" + str(i) + ".png"
            cv.imwrite(save_name, monitor_img)


