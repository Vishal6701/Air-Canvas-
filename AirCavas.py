import cv2
import numpy as np
import Hand_Tracking_Module as htm 
import pyautogui
import math
import time
import os
pyautogui.FAILSAFE=False
detector=htm.handDetector(detectionCon=0.7)
cap=cv2.VideoCapture(0)
###########################################
folderPath="photo"
mylist=os.listdir(folderPath)
#print(mylist)
overLay=[]
for impath in mylist:
     image=cv2.imread(f'{folderPath}/{impath}')
     overLay.append(image)

Header=overLay[0]
eraserThickness=40
###################
imgCanvas=np.zeros((480,640,3),np.uint8)
drawColor=(255,0,255)
xp,yp=0,0
while True:
    success,img=cap.read()
    img=cv2.flip(img,+1)
    hand=detector.findHands(img)
    location,bbox=detector.findPosition(img,draw=False)
    if len(location)!=0:
        x1,y1=location[8][1],location[8][2]
        x2,y2=location[12][1],location[12][2]
        finger=detector.fingerUp()
       

        # Selection mode 
        if finger[1] and finger[2]:
            
            print("selection mode")

            if y1<63:
                
                if  60<x1<150:
                    Header=overLay[0]
                    drawColor=(0,0,255)

                elif  200<x1<280:
                    Header=overLay[1]
                    drawColor=(51,255,51)

                elif  335<x1<430:
                    Header=overLay[2]
                    drawColor=(0,255,255)

                elif  490<x1<590:
                    Header=overLay[3]
                    drawColor=(0,0,0)
            cv2.rectangle(img,(x1,y1-25),(x2,y2+25),drawColor,cv2.FILLED)


        if finger[1] and finger[2]==False:
            cv2.circle(img,(x1,y1),10,drawColor,cv2.FILLED)
            if xp == 0 and yp == 0:
                xp,yp= x1,y1  
            if drawColor==(0,0,0):
                cv2.line(img, (xp,yp),(x1,y1),drawColor, eraserThickness)
                cv2.line(imgCanvas, (xp,yp),(x1,y1),drawColor, eraserThickness)
            else:
                cv2.line(img, (xp,yp),(x1,y1),drawColor, 4)
                cv2.line(imgCanvas, (xp,yp),(x1,y1),drawColor, 4)
            xp,yp=x1,y1
    else :
        xp,yp=0,0
       

            
                
   

  
   

      
    ############### Drawing Mode #################
      
      
    ###################################################################
    img = cv2.add(img,imgCanvas)
    img[0:63  , 0:640]=Header
    #stacked = np.hstack((canvas,img))
    #cv2.imshow('VIRTUAL PEN',cv2.resize(stacked,None,fx=0.6,fy=0.6))
      


     
    
    cv2.imshow("out",img)
    #cv2.imshow("output2",imgCanvas)

    

    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()
