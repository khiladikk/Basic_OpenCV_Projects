#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing libraries
import cv2


# In[2]:


# using pre-trained haar cascade xml file 
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")


# In[3]:


# loading the image
image = cv2.imread("heros.jpg")

# converting the image to BGR to HSV
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# In[4]:


# detecting different size of image in the image
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    
    # to draw rectangle around in the face and eye
    image = cv2.rectangle(image, (x,y), (x+w , y+h), (255,0,0),2)
    
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]
    
    eyes = eye_cascade.detectMultiScale(roi_gray)
    
    # detecting different size of eyes in the image
    for (ex,ey,eh,ew) in eyes:
        
        cv2.rectangle(roi_color, (ex,ey),(ex+ew, ey+eh), (0,255,0), 2)


# In[5]:


# displaying the image
cv2.imshow('image', image)

# waiting for "s" key to stop the operation
k = cv2.waitKey(0)
stop = ord("S")
if k == stop:
    cv2.destroyAllWindows()

# quitting the operation    
elif k == ord('q'):
    cv2.imwrite('marked1.png',image)
    
# closing all the open GUIs    
    cv2.destroyAllWindows()
    


# In[ ]:




