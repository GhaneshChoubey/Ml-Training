# GUI -Graphical User Interface

# Liraries
#####################
#1.Tkinter
# 2.PyQt
# 3.Turtle

from tkinter import ttk
import tkinter as ttk

app=ttk.Tk()
app.title("My App")
app.geometry('600x400')

ttk.Label(app,text = 'A simple Text Label').place(x=50,y=50)

ttk.Label(app,text = 'Ghanesh is a best progammer in the world').place(x=50,y=70)
app.mainloop()