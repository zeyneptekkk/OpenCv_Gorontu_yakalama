import cv2
import numpy as np

img=cv2.imread("resimm.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
Canny=cv2.Canny(gray,150,150)

cv2.imshow("resim",Canny)
contours,_=cv2.findContours(Canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

for cnt in contours:
    area=cv2.contourArea(cnt)
    if area>100:

        approx=cv2.approxPolyDP(cnt,0.025*cv2.arcLength(cnt, True),True)
        cornerCount = len(approx)
        x, y, w, h = cv2.boundingRect(approx)
        if(cornerCount==3):
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 5)
            cv2.putText(img,"Ucgen",(x+10,y+10),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0))
        elif (cornerCount == 4):
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 5)
            cv2.putText(img, "Dikdortgen", (x + 10, y + 10), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0))
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 5)
            cv2.putText(img, "Bilinmeyen", (x + 10, y + 10), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0))
        cv2.drawContours(img,cnt,-1,(0,255,0),3)




cv2.imshow("Resim",img)


cv2.waitKey(0)