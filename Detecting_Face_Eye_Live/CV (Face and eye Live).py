#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing the library
import cv2


# In[2]:


# Using the pre-trained haar cascade XML file
# for face and eyes separately
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")


# In[3]:


# capturing the each frames from the webcam
cap =cv2.VideoCapture(0)


# In[4]:


# using the while loop(infinite loop)
while True:
    
    # capturing frame by frame from the webcam
    ret, img = cap.read()
    
    # converting the image from BGR to GRAY scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # creating a rectangle around the face and eyes
    # using the coordinates 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:
        
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255),2)
        
        roi_gray = gray[y:y+h ,x:x+h]
        roi_color = img[y:y+h , x:x+w]
        
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        
        # detecting different size of eyes in the image
        for (ex,ey,eh,ew) in eyes:
            cv2.rectangle(roi_color, (ex,ey),(ex+ew, ey+eh), (0,255,0), 2)
            
    # showing the output window    
    cv2.imshow('img',img)
    
    # using the waitkey command to close the opend GUIs
    k = cv2.waitKey(30)
    stop = ord('s')
    if k == stop:
        break
            


# In[5]:


# releasing the captured frames
cap.release()    


# In[6]:


# closing all the opended windows and GUIs
cv2.destroyAllWindows()
OPENCV_VIDEOIO_PRIORITY_MSMF = 0

