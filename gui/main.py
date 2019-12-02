#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import lifegame as lg
import matplotlib.pyplot as plt
import tkinter as tk
import cv2
#import lggraph 
#get_ipython().run_line_magic('reload_ext', 'autoreload')
#get_ipython().run_line_magic('autoreload', '2')

def btn_click():
    #print("I clicked")
    cell.step()
    #cell.cell=cell.ncell
    #plt.imshow(cell.cell)
    cell.graphic()
    #j=1
    #print(j)
    #j=j+1
    #if tago==1 :
    root.after(5,btn_click)
def btn_stop():
    root.quit()
    exit()
    #plt.imshow(np.transpose(cell.cell))
#cellを定義
m=100
n=100
#cellのwidthを指定
wcell=5
#tago=1
#cellを定義
#cell=lg.cells(m,n)
#画面起動
root=tk.Tk()
root.title(u"LifeGame by Tago")
root.geometry("1200x800")
canvas=tk.Canvas(root,width=m*wcell,height=n*wcell,bg="black")
canvas.place(x=0,y=0)
for j in range(n):
    for i in range(m):
        canvas.create_rectangle(wcell*i, wcell*j,wcell*(i+1),wcell*(j+1),outline='white',fill='', width=1)

cell=lg.cells(m,n,wcell,canvas)
canvas.bind("<Button-1>", cell.click)

#初期条件を左上グライダーにする
#cell.init_glider()
btn = tk.Button(root, text='start',command=btn_click)
btn.place(x=800, y=300)
btn2 =tk.Button(root,text='stop',command=btn_stop)
btn2.place(x=800, y=400)
root.mainloop()


# In[ ]:




