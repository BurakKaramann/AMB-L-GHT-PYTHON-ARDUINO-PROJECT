import serial

import time
import pyautogui
from PIL import ImageGrab,Image
import cv2
import numpy as np

bluetooth = serial.Serial(port = "COM8", baudrate= 9600, timeout= 1) # serial

while True: 
    x,y=pyautogui.size() #1920x1080
    img=ImageGrab.grab(bbox=(0,0,int(x),int(y)))    
    screen =cv2.cvtColor(np.array(img),cv2.COLOR_RGB2BGR)
    
    H,W,B = screen.shape
    T_bgr_b,T_bgr_g,T_bgr_r=0,0,0
    start=time.time()

    for h in range(0,H,5):
        for w in range(0,W,5):         
            T_bgr_b += screen[(h,w)][0]
            T_bgr_g += screen[(h,w)][1]
            T_bgr_r += screen[(h,w)][2]
    
    O_bgr_b,O_bgr_g,O_bgr_r=int( T_bgr_b/((H*W)/25) ),int( T_bgr_g/((H*W)/25) ),int( T_bgr_r/((H*W)/25) )

    end=time.time()
    Sure=end-start
    print("B : {0} , G : {1} R : {2}  SURE :  {3} ".format(O_bgr_b,O_bgr_g,O_bgr_r,Sure))
    a= str(O_bgr_r) +""+ str(O_bgr_g) + "," +str(O_bgr_b) + "\n"
    #a= str(0) +","+ str(0) + "," +str(255) + "\n"
    
    bluetooth.write(str(a).encode('ascii')) # Serial
    #cv2.imshow('Python Window', screen)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break