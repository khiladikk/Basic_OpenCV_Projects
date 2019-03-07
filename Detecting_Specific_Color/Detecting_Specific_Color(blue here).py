#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Importing the Libraries
import cv2
import numpy as np


# In[10]:


# Capturing webcam frames
cap = cv2.VideoCapture(0)


# In[11]:


# Settingup the lower threshold
param1 = [100,100,100]
# setting the upper threshold
param2 = [150,150,255]


# In[12]:


# using infinite loop
while(1):
    
    # capturing frame by frame from the webcam
    ret, frame = cap.read()
    
    # Converting Images from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array(param1)
    upper = np.array(param2)
    
    # Defining range of blue color in HSV
    # creating mask of blue color objects found in the frame
    mask = cv2.inRange(hsv, lower, upper)
    
    # finishing the bitwise_end of the frame and mask
    # highlighting and storing the bluecolor objects in res 
    res = cv2.bitwise_and(frame, frame, mask = mask)
    
    # this display the frame, mask and
    # res in 3 separate windows
    cv2.imshow('Picture', frame)
    cv2.imshow('Res', res)
    cv2.imshow('Maks', mask)
    
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    # using 's' command to close the all open HighGUI windows   
    elif k == ord('s'):
        cv2.destroyAllWindows()
        cap.release()


# In[ ]:





# In[ ]:




