import numpy as np
import cv2 
from math import sqrt



"""
Burada 2 farklı şekilde blur aldım çünkü içbükeyi bulurken diğer bulur biraz yetersiz kaldı
"""


font=cv2.FONT_HERSHEY_COMPLEX
ilk = cv2.imread("deneme.jpg") 
img2=cv2.imread("deneme.jpg")
img = cv2.GaussianBlur(ilk,(11,13),0)
imgic=cv2.GaussianBlur(ilk,(13,13),0)
bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
bwic=cv2.cvtColor(imgic, cv2.COLOR_BGR2GRAY) 


ret, bw=cv2.threshold(bw,80,255,cv2.THRESH_BINARY)
ret, bwic=cv2.threshold(bwic,80,255,cv2.THRESH_BINARY_INV)


contours, hierarchy = cv2.findContours(bwic, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)  






"""
Burada Matrise  siyah beyaz olmasına göre 0 ve 1 değerlerini atadım
"""

sutun, satır = 800, 600;
Matrix = [[0 for x in range(sutun)] for y in range(satır)] 

for x in range (600):
    for y in range(800):
        if(bw[x,y])==255:
            Matrix[x][y]=0
            
        else:
            Matrix[x][y]=1




say=0;
"""
burada köşeleri karşılaştırdım komşularıyla ve ona göre köşe sayısını buldum

"""
diskenar=[]
for x in range (600):
    for y in range(800):
        numberOfzero=0
        
        if Matrix[x][y]==1:
            if x>2 and x<598 and y>2 and y<798:
                for w in range (5):
                    for q in range(5):
                        if Matrix[x-2+w][y-2+q]==0:
                            numberOfzero=numberOfzero+1
            if numberOfzero>12:
                diskenar.append((x,y))
                
  
                cv2.circle(img2,(y,x),1,(0,0,255),-1)
                say=say+1  
                for a in range (5):
                    for b in range(5):
                        if Matrix[x-2+a][y-2+b]==0:
                            Matrix[x-2+a][y-2+b]=2
                        



sutun, satır = 800, 600;
Matrix = [[0 for x in range(sutun)] for y in range(satır)] 

for x in range (600):
    for y in range(800):
        if(bwic[x,y])==255:
            Matrix[x][y]=0
            
        else:
            Matrix[x][y]=1




sayic=0;

for x in range (600):
    for y in range(800):
        numberOfzero=0
        
        if Matrix[x][y]==1:
            if x>2 and x<598 and y>2 and y<798:
                for w in range (5):
                    for q in range(5):
                        if Matrix[x-2+w][y-2+q]==0:
                            numberOfzero=numberOfzero+1
            if numberOfzero>12:
                cv2.circle(img2,(y,x),1,(0,0,255),-1)
                sayic=sayic+1
                diskenar.append((x,y))
                for a in range (5):
                    for b in range(5):
                        if Matrix[x-2+a][y-2+b]==0:
                            Matrix[x-2+a][y-2+b]=2
              
         




buyuksayix=0
buyuksayiy=0
kucuksayix=1000
kucuksayiy=1000

"""
burda da contourların en büyük ve en küçük değerlini buldum ve ona göre karşılaştırma yaptım

"""

for kac in range(6): 
    
    buyuksayix=0
    buyuksayiy=0
    kucuksayix=1000
    kucuksayiy=1000 
    topla=0           
    for contour in range(len(contours[kac])):
        if contours[kac][contour][0][0]>buyuksayix:
            buyuksayix=contours[kac][contour][0][0]
                
    for contour in range(len(contours[kac])):
        if contours[kac][contour][0][1]>buyuksayiy:
            buyuksayiy=contours[kac][contour][0][1]
                
                
    for contour in range(len(contours[kac])):
            if contours[kac][contour][0][1]<kucuksayiy:
                kucuksayiy=contours[kac][contour][0][1]
                
    for contour in range(len(contours[kac])):
            if contours[kac][contour][0][0]<kucuksayix:
                kucuksayix=contours[kac][contour][0][0]
    
               
      
   
    for x in range (kucuksayix-10,buyuksayix+10):
            for y in range (kucuksayiy-10,buyuksayiy+10):
                for q in range (len(diskenar)):
                    if y == diskenar[q][0] and x == diskenar[q][1]:
                        topla=topla+1
          
    yazx=int(((buyuksayix+kucuksayix)/2)-50)
    yazy=int((buyuksayiy+kucuksayiy)/2)
    if topla<2:
        cv2.putText(ilk,"yuvarlak",(yazx,yazy),font,1,(0, 0, 255))
    elif topla==3:
        cv2.putText(ilk,"ucgen",(yazx,yazy),font,1,(0, 0, 255))
    elif topla==4:
        cv2.putText(ilk,"kare",(yazx,yazy),font,1,(0, 0, 255))
    elif topla==5:
        cv2.putText(ilk,"besgen",(yazx,yazy),font,1,(0, 0, 255))
    elif topla==6:
        cv2.putText(ilk,"altigen",(yazx,yazy),font,1,(0, 0, 255))
    elif topla>6:
        cv2.putText(ilk,"yildiz",(yazx,yazy),font,1,(0, 0, 255))
        
    

          

cv2.imshow("img2",ilk)




cv2.waitKey(0)

cv2.destroyAllWindows()





