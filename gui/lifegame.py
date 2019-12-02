#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
import tkinter as tk
from multiprocessing import Pool
import cv2
from numba import jit


# In[14]:


#@jit
class cells:
    def __init__(self,m,n,w,canvas):
        #初期セル配置は常にゼロ
        #selfのセルにデータを格納
        self.cell=np.zeros((m+2,n+2),dtype=np.uint16)
        self.ncell=np.zeros((m+2,n+2),dtype=np.uint16)
        self.height=m
        self.width=n
        self.cellsize=w
        self.canvas=canvas
        self.kernel = np.array([[1,1,1],[1,0,1],[1,1,1]], dtype=np.uint16)

        #運命関数の定義
        #self.dest=np.zeros((256,2),dtype=int)
        #self.dest=self.fate()
        #for i in range(256):
        #    print(i,self.dest[i])
    #初期条件として左上にグライダーを設定
    def init_glider(self):
        self.cell[0,0]=1
        self.cell[1,1]=1
        self.cell[1,2]=1
        self.cell[2,0]=1
        self.cell[2,1]=1
    def click(self,event):
        x1=event.x//self.cellsize
        y1=event.y//self.cellsize
        #描画
        tag='cell'+str(self.height*x1+y1)
        if self.cell[x1+1,y1+1]==0:
            self.canvas.create_rectangle(self.cellsize*x1, self.cellsize*y1, self.cellsize*x1+self.cellsize, self.cellsize*y1+self.cellsize,outline='black',tag=tag,fill='lime', width=1)
            self.cell[x1+1,y1+1]=1
        else:
            self.canvas.delete(tag)
            self.cell[x1+1,y1+1]=0
   # def fate(self):
   #     d=np.zeros((256,2),dtype=int)
   #     for i in range(256):
   #         a=np.zeros(8,dtype=int)
   #         c=np.zeros(3,dtype=int)
   #         n=i
   #         j=1
   #         #a=0
   #         while n>0:
   #             a[8-j]=n%2
   #             n=n//2
   #             j=j+1
   #         b=np.sum(a)
   #         n=b
   #         j=1
   #         #c=0
   #         while n>0:
   #             c[3-j]=n%2
   #             n=n//2
   #             j=j+1
   #         #determine fate
   #         d[i,0]=c[1]*c[2]*(-c[0]+1)
   #         d[i,1]=(-c[0]+1)*c[1]
   #     return d    
    def step(self):
        a=cv2.filter2D(self.cell, -1, self.kernel)
        #print(a)
        alive = (self.cell == 1) * ((a == 2) + (a == 3))*1
        born  = (self.cell == 0) * (a == 3)*1
        
        self.ncell=alive+born
        
        self.cell=self.ncell.astype(np.uint16)
        #for j in range(self.width):
        #    for i in range(self.height):
        #        self.cell[i,j]=self.ncell[i,j]
        #        print(self.cell[i,j]-self.ncell2[i,j])
        #elf.cell=
    def graphic(self):
        self.canvas.delete("all")
        for j in range(self.width):
            for i in range(self.height):
                if self.cell[i+1,j+1]==1:
                     self.canvas.create_rectangle(self.cellsize*i, self.cellsize*j, self.cellsize*i+self.cellsize, self.cellsize*j+self.cellsize,outline="black",fill='lime', width=1)            


# In[111]:


#cellを定義
#m=25
#n=25
#cellのwidthを指定
#wcell=20
#cellを定義
#cell=lg.cells(m,n)
#画面起動
#root=tk.Tk()
#root.title(u"LifeGame by Tago")
#root.geometry("800x600")
#canvas=tk.Canvas(root,width=m*wcell,height=n*wcell,bg="black")
#canvas.place(x=0,y=0)
#a=cells(m,n,wcell,canvas)


# In[31]:


#m=10
#n=10
#cell=np.ones((3,3),np.float32)
#kernel = np.array([[1,1,1],[1,0,1],[1,1,1]], dtype=int)
#a=cv2.filter2D(cell, -1, kernel)
#print(a)
#a=a.astype(np.int)
#print(a)


# In[ ]:




