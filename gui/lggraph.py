#!/usr/bin/env python
# coding: utf-8

# In[9]:


import tkinter as tk


# In[39]:


#click関数を定義
class lggraph :
    def __init__(self,m,n,w,canvas):
        self.height=m
        self.width=n
        self.cellwidth=w
        #画面セット
        self.canvas=canvas
        print(self.height)
    def click(self,event):
        x1=event.x//self.cellwidth
        y1=event.y//self.cellwidth
        self.canvas.create_rectangle(self.cellwidth*x1, self.cellwidth*y1, self.cellwidth*x1+self.cellwidth, self.cellwidth*y1+self.cellwidth,outline='black',fill='lime', width=1)


# In[ ]:




