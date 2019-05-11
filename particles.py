from random import randint
import numpy as np


class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def tick(self, mask):
        left, right, buttomleft, buttom, buttomright = self.preprocess(mask)

        if buttom == 0:
            self.x += randint(1, 2)
            return

        if buttom == 255 and buttomright == 0:
            self.x += randint(1, 2)
            self.y += randint(1, 2)
            return

        if buttom == 255 and buttomleft == 0:
            self.x += randint(1, 2)
            self.y -= randint(1, 2)

    def all_in_white(self, mask):
        try:
            square = mask[self.x-3:self.x+3, self.y-3:self.y+3]
            unique, counts = np.unique(square, return_counts=True)
            z = dict(zip(unique, counts))
            if 255 in z.keys() and z[255] > 34:
                return True
            return False
        except:
            return True

    def preprocess(self, mask):
        my_mask = mask.copy()
        x = self.x
        y = self.y
        try:
            left = my_mask[x, y-1]
        except:
            left = 0

        try:
            right = my_mask[x, y+1]
        except:
            right = 0

        try:
            buttomleft = my_mask[x+1, y-1]
        except:
            buttomleft = 0

        try:
            buttom = my_mask[x+1, y]
        except:
            buttom = 0

        try:
            buttomright = my_mask[x+1, y+1]
        except:
            buttomright = 0

        return left, right, buttomleft, buttom, buttomright
