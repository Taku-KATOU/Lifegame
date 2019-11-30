#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk


# In[14]:


#generate window
root=tk.Tk()
#window title
root.title(u"GUI_Test")
#window size
root.geometry("400x400")

#label
Static1 = tk.Label(text=u'test')
Static1.pack()

button= tk.Button(text='set')
button.pack()
root.mainloop()


# In[ ]:




