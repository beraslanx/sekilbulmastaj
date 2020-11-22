import cv2
import numpy as np



img=cv2.imread("golgeli.jpg")
ilk=cv2.imread("golgeli.jpg")
 

imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, img125=cv2.threshold(imggray,125,255,cv2.THRESH_BINARY)
ret, img25=cv2.threshold(imggray,15,255,cv2.THRESH_BINARY)

#burada 2 farklı threshold uyguluyorum sağı ve solundaki şekilleri daha iyi alabilmek için

#alt kısımda gölgenin başladığı ksıımdan bittiği kısıma bir çizgi çekip sağda kalan siyahları alıp daha önce solda olanlara ekliyorum
for y in range(800):
    if img125[1][y]==255 and img125[1][y-1]==0:
        ilky=y
    if img125[598][y]==255 and img125[598][y-1]==0:
        sony=y



cv2.line(img,(ilky,0),(sony+2,600),(255,0,0),1)


if img[ilky][0][0]==255:
    print("evet")

for x in range (600):
    yeniy=5999
    for y in range(800):
        if y>yeniy:
            img25[x][y]=img125[x][y]
        if img[x][y][0]==255 and img[x][y][1]==0 and img[x][y][2]==0:
            yeniy=y
  
                  
                   
        
       
       

      

       



#bundan sonrası eski kod zaten




font=cv2.FONT_HERSHEY_COMPLEX

img = cv2.GaussianBlur(img25,(11,15),0)
imgic=cv2.GaussianBlur(img25,(17,15),0)



ret, bw=cv2.threshold(img,80,255,cv2.THRESH_BINARY)
ret, bwic=cv2.threshold(imgic,80,255,cv2.THRESH_BINARY_INV)


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