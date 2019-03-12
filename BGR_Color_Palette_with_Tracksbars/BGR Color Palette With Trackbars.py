#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Importing the libraries
import cv2
import numpy as np

# calling empty function whenever trackbar moves
def emptyFunction():
    pass

def main():
    
# A blackwindow of three color channels
    img= np.zeros((512,512,3), np.uint8)


    windowname = "BGR color palette"

    # Window name
    cv2.namedWindow(windowname)

    # Trackbars name with their minimum and maximum value
    cv2.createTrackbar('B', windowname, 0, 255, emptyFunction)
    cv2.createTrackbar('G', windowname, 0, 255, emptyFunction)
    cv2.createTrackbar('R', windowname, 0, 255, emptyFunction)

    # used to open the GUI window 
    # till ESC press to exit key
    while(True):
        cv2.imshow("BGR color palette", img)
        
        
        
        if cv2.waitKey(1) == 27:
                    break 
        
        # Value of blue green and red   
        blue = cv2.getTrackbarPos('B', "BGR color palette")
        green = cv2.getTrackbarPos('G', "BGR color palette")
        red = cv2.getTrackbarPos('R', "BGR color palette")
        
        # merging all the colors channels and make 
        # the image composites form the RGB
        img[:] = [blue, green, red]
        print(blue, green, red)
        
# closing all the windows            
cv2.destroyAllWindows()


# calling main
if __name__ == "__main__":
    main()
    


# In[ ]:




