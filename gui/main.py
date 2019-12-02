#!/usr/bin/env python
# coding: utf-8

# In[56]:


import numpy as np
import lifegame as lg
import matplotlib.pyplot as plt
import tkinter as tk
import cv2
from numba import jit
#import time
#import threading
#import lggraph 
#%reload_ext autoreload
#%autoreload 2
#@jit
def sloop():
    
    #while not stop_flag:
    cell.step()
    cell.graphic()
    root.after(10,sloop)
    

def btn_click():
    global stop_flag
    global thread
    
    sloop()
    
def btn_stop():
    global stop_flag
    global thread
    
    #if thread:
    #    stop_flag=True

    #plt.imshow(np.transpose(cell.cell))
#cellを定義
m=10
n=10
wcell=10
#画面サイズ
width=m*wcell+100
height=n*wcell+100
#cellのwidthを指定

#tago=1
#cellを定義
#cell=lg.cells(m,n)
#画面起動
root=tk.Tk()
root.title(u"LifeGame by Tago")
root.geometry(str(width)+"x"+str(height))
canvas=tk.Canvas(root,width=m*wcell,height=n*wcell,bg="black")
canvas.place(x=0,y=0)
for j in range(n):
    for i in range(m):
        canvas.create_rectangle(wcell*i, wcell*j,wcell*(i+1),wcell*(j+1),outline='white',fill='', width=1)

cell=lg.cells(m,n,wcell,canvas)
canvas.bind("<Button-1>", cell.click)

#初期条件を左上グライダーにする
#cell.init_glider()
#thread=None
stop_flag=False
btn = tk.Button(root, text='start',command=sloop)
btn.place(x=str(width*4/5), y=str(height/2))
btn2 =tk.Button(root,text='stop',command=btn_stop)
btn2.place(x=str(width*4/5), y=str(height/2+100))
root.mainloop()
#stop_flag=True
#thread.join()


# In[ ]:





# In[ ]:





# In[ ]:




