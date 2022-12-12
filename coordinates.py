import time
import numpy as np
import pyscreenshot as ImageGrab
import cv2
import os

def photo():
    filename = 'pasport-test.png'
    x = 1
    last_name = time.time()

    while(True):
        screen = np.array(ImageGrab.grab(bbox=(1228,423 ,1327,498)))
        #print('look tool {} second'.format(time.time()-last_name))
        last_time = time.time()
        cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        cv2.imwrite(filename, screen)
        x = x + 1
        #print(x)
        if x == 2:
            cv2.destroyAllWindows()
            break