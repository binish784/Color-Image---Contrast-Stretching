"""
Created on Tue Oct 30 11:16:51 2018

@author: Binish125
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('inputImage2.jpg')

pix_number=np.ma.count(img)
print("number of pixels : " +str(pix_number))


number_of_cols=int(img[1].size/3)
number_of_rows=(int(np.ma.count(img)/img[1].size))

#rgbCombined=np.random.randint(0,1,size=(number_of_rows,number_of_cols))

newImage=np.random.randint(0,1,size=(number_of_rows,number_of_cols,3))
RedOnly=np.random.randint(0, 1, size=(number_of_rows, number_of_cols))
GreenOnly=np.random.randint(0, 1, size=(number_of_rows, number_of_cols))
BlueOnly=np.random.randint(0, 1, size=(number_of_rows, number_of_cols))

print(img)
print(number_of_cols)
print(number_of_rows)

for i in range(number_of_rows):
    for j in range(number_of_cols):
        BlueOnly[i][j]=img[i][j][0]
        GreenOnly[i][j]=img[i][j][1]
        RedOnly[i][j]=img[i][j][2]
        
        #BlueOnly[i][j]=[img[i][j][0],0,0]
        #GreenOnly[i][j]=[0,img[i][j][1],0]
        

#cv2.imwrite('greenOnly.jpg',GreenOnly)
#cv2.imwrite('redOnly.jpg',RedOnly)
#cv2.imwrite('blueOnly.jpg',BlueOnly)
        

x,a,d=plt.hist(BlueOnly.ravel(),256,[0,256],label='x')
y,b,e=plt.hist(GreenOnly.ravel(),256,[0,256],label='y')
z,c,f=plt.hist(RedOnly.ravel(),256,[0,256],label='z')

arr=[x,y,z]

k=[0,0,0]
k[0]=np.sum(x)
k[1]=np.sum(y)
k[2]=np.sum(z)

prk_list=[]
prk_list.append([])
prk_list.append([])
prk_list.append([])
sk_list=[]
sk_list.append([])
sk_list.append([])
sk_list.append([])
last_list=[]
last_list.append([])
last_list.append([])
last_list.append([])
L=256
sk=[0,0,0]


for n in range(3):
    for i in range(len(x)):
        prk=arr[n][i]/k[n]
        sk[n]=prk+sk[n]
        last=(L-1)*sk[n]
        if last!=0:
            rem=int(last % last)
        else:
            rem=0
        if rem >=0.5:
            last=int(last)+1
        else:
            last=int(last)
        prk_list[n].append(prk)
        sk_list[n].append(sk[n])
        last_list[n].append(last)
            
for i in range(number_of_rows):
    for j in range(number_of_cols):
        num_red=RedOnly[i][j]
        if num_red != last_list[2][num_red]:
            RedOnly[i][j]=last_list[2][num_red]
        num_green=GreenOnly[i][j]
        if num_green != last_list[1][num_green]:
            GreenOnly[i][j]=last_list[1][num_green]
        num_blue=BlueOnly[i][j]
        if num_blue != last_list[0][num_blue]:
            BlueOnly[i][j]=last_list[0][num_blue]
        newImage[i][j]=[BlueOnly[i][j],GreenOnly[i][j],RedOnly[i][j]]


cv2.imwrite("newSat.jpg",newImage)