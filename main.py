import numpy as np
import cv2
from random import randint
from particles import Particle


cap = cv2.VideoCapture(0)
ret, frame = cap.read()
rows, cols, channels = frame.shape
fgbg = cv2.createBackgroundSubtractorKNN()
ps = [Particle(10, 240)]
drop = cv2.imread('drop.png')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (cols, rows))

while(True):
    random = randint(1, 20)
    if random <= 9:
        x = randint(10, 50)
        y = randint(10, cols-20)
        ps.append(Particle(x, y))
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    temp = fgmask.copy()
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
    morph_img = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)
    morph_img = cv2.morphologyEx(morph_img, cv2.MORPH_OPEN, kernel)
    ret, morph_img = cv2.threshold(morph_img, 220, 255, cv2.THRESH_BINARY)

    for p in ps:
        try:
            frame[p.x-5:p.x, p.y-5:p.y] = drop
        except:
            ps.remove(p)

    out.write(frame)
    cv2.imshow('frame', frame)
    # cv2.imshow('morph', morph_img)


    for p in ps:
        p.tick(morph_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
