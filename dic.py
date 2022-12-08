import cv2
import numpy as np
import matplotlib.pyplot as plt
im=cv2.imread("C:\\eytr\\PB_Task3A_Windows\\test_images\\maze_000.png")
img=cv2.cvtColor(im,cv2.COLOR_RGB2HSV)
l=np.array([[[110,255,255]]])
r=np.array([[[130,255,255]]])
k=cv2.inRange(img,l,r)
h=np.array([[[255,0,0]]],dtype='uint8')
h=cv2.cvtColor(h,cv2.COLOR_BGR2HSV)
plt.imshow(k)
c=cv2.findContours(k,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
lst=[]
for i in range(len(c[0])):
    lst.append(list(c[0][i][0].tolist()))
im=cv2.imread("C:\\eytr\\PB_Task3A_Windows\\test_images\\maze_001.png")
img=cv2.cvtColor(im,cv2.COLOR_RGB2HSV)
l=np.array([[[110,255,255]]])
r=np.array([[[130,255,255]]])
k=cv2.inRange(img,l,r)
c=cv2.findContours(k,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
lst=[]
for i in range(len(c[0])):
    lst.append(list(c[0][i][0].tolist()))
nodes=['A','B','C','D','E','F']
nodes1=['1','2','3','4','5','6']
lst1=[]
for i in range(len(lst)):
    a=str(lst[i][0][0]+6)
    b=str(lst[i][0][1]+6)
    lst1.append(nodes[(int(a[0]))-1]+''+nodes1[(int(b[0]))-1])
im=cv2.imread("C:\\eytr\\PB_Task3A_Windows\\test_images\\maze_001.png")
img=cv2.cvtColor(im,cv2.COLOR_RGB2HSV)
l=np.array([[[50,255,255]]])
r=np.array([[[70,255,255]]])
k=cv2.inRange(img,l,r)
c=cv2.findContours(k,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
lst=[]
for i in range(len(c[0])):
    if c[0][i][0][0][1]>200:
        lst.append(list(c[0][i][0].tolist()))
nodes=['A','B','C','D','E','F']
nodes1=['1','2','3','4','5','6']
lst1=[]
for i in range(len(lst)):
    a=str(lst[i][0][0]+6)
    b=str(lst[i][0][1]+6)
    lst1.append(nodes[(int(a[0]))-1]+''+nodes1[(int(b[0]))-1])
print(lst1)
im='C:\\eytr\\PB_Task3A_Windows\\test_images\\maze_000.png'
im=cv2.imread(im)
plt.imshow(im)
lst=['A','B','C','D','E','F']
lst2=['6','5','4','3','2','1']
lst1=[]
im=cv2.rotate(im,cv2.ROTATE_90_CLOCKWISE)
dic1={}
i=594
j=624

count=0
while i>=0 and j>=0:
    x=120
    y=180
    while x<=600 and y<=600:
       
        img=im[i:j,x:y]
        x=x+100
        y=y+100
    
        img=cv2.Canny(img,125,175)
        contours,heirarchies=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        if len(contours)==0:
            count=count+1
            a=lst[((i)//100)]
          
            b=lst2[(x-100)//100]
            b=int(b)+1
            e=lst2[((x-100)//100)+1]
            e=int(e)+1
            c=a+str(e)+'-'+a+str(b)
            s=a+str(e)
            t=a+str(b)
            nd=[s]
            
           
            nd1=[t]
            
            if s in dic1.keys(): dic1[s].extend(nd1)
            else: dic1[s]=nd1
             
            if t in dic1.keys(): dic1[t].extend(nd)
            else: dic1[t]=nd
            lst1.append(c)
            
    i=i-100
    j=j-100
lst1.sort()
#dic1['horizontal road block']=lst1 
   
print(dic1)
im='C:\\eytr\\PB_Task3A_Windows\\test_images\\maze_000.png'
im=cv2.imread(im)
lst=['A','B','C','D','E','F']
lst1=[]
c=[]
f=[]
dic={}
i=594
j=624
count=0
while i>=0 and j>=0:
    x=120
    y=180
    while x<=600 and y<=600:
       
        img=im[i:j,x:y]
        x=x+100
        y=y+100
    
        img=cv2.Canny(img,125,175)
        contours,heirarchies=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        if len(contours)==0:
            count=count+1
            a=lst[((x-100)//100)-1]
            d=lst[((x-100)//100)]
            b=i//100
            s=a+str(b+1)
            t=(d+str(b+1))
            nd=[s]
            
            print(nd)
            nd1=[t]
            
            if s in dic.keys(): dic[s].extend(nd1)
            else: dic[s]=nd1
            if t in dic.keys(): dic[t].extend(nd)
            else: dic[t]=nd
            
            c.append(nd)
            f.append(nd1)
            

            
    i=i-100
    j=j-100
lst1.append(c)
lst1.append(f)

#dic['vertical road block']=lst1 
   
print(dic)
lst=['A','B','C','D','E','F']
i=0

dick={}
print(dic1['B5'])
while i <6:
    
    s1=''
    j=0
    while j<6:
        s1=lst[i]+str(j+1)
        adjlis=[]
        if(i+1<6):
            s=lst[i+1]+str(j+1)
            if (s not in dic.keys() or s1 not in dic[s]) and (s not in dic1.keys() or s1 not in dic1[s]):
                adjlis.append(s)
        if(j+1<6):
            s=lst[i]+str(j+1+1)
            if (s not in dic.keys() or s1 not in dic[s]) and (s not in dic1.keys() or s1 not in dic1[s]):
                adjlis.append(s)
        if(i-1>=0):
            s=lst[i-1]+str(j+1)
            if (s not in dic.keys() or s1 not in dic[s]) and (s not in dic1.keys() or s1 not in dic1[s]):
                adjlis.append(s)
        if(j-1>=0):
            s=lst[i]+str(j)
            if (s not in dic.keys() or s1 not in dic[s]) and (s not in dic1.keys() or s1 not in dic1[s]):
                adjlis.append(s)
        j+=1
        dick[s1]=adjlis
    i+=1
print(dick)
im='C:\\eytr\\PB_Task3A_Windows\\test_images\\maze_000.png'
im=cv2.imread(im)
purple=np.array([[[128,0,128]]],dtype='uint8')
purple=cv2.cvtColor(purple,cv2.COLOR_RGB2HSV)
im4=cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
im1=cv2.cvtColor(im4,cv2.COLOR_RGB2HSV)
print(purple)
l=np.array([[[120,255,128]]],dtype='uint8')
r=np.array([[[250 ,255 ,128]]],dtype='uint8')
im2=cv2.inRange(im1,l,r)
CNT=cv2.findContours(im2,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
print(CNT)
x=str(CNT[0][0][0][0][0]+6)
temp=x[0]
x=str(CNT[0][0][0][0][1]+6)
temp1=x[0]
lst=['A','B','C','D','E','F']
stpnode=lst[int(temp)-1]+temp1
print(stpnode)
plt.imshow(im4)
