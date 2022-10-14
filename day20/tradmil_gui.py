import imp
from optparse import Values
from pydoc import plain
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as ttk

app=ttk.Tk()
app.geometry('600x300')
app.title("Treadmil Users Aanalysis")

graphs=ttk.Variable(app)
values={'Data':'1','Data 2':'2'}
for key, value in values.items():
    ttk.Radiobutton(app,text=key,variable=graphs,value=value).pack()


def show():
    print(graphs.get())

ttk.Button(app,text='Show',command=show).place(x=400,y=10)



app.mainloop()
