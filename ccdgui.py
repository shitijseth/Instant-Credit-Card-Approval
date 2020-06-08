##All the libraries##
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from tkinter import *
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pyplot import imread
from openpyxl import load_workbook
import random
from random import shuffle
import itertools


##GUI using Tkinter##
window = Tk()

#Window Title
window.title("Credit Card Application Predictor")

window.geometry('500x800')

yval=5

#First Name
lbl3 = Label(window, text = "Enter first name ->")
lbl3.grid(row=0, column=0)
first_name = StringVar()
fn = Entry(textvariable=first_name)
fn.grid(row=0, column=1, pady=yval)

#Last Name
lbl4 = Label(window, text = "Enter last name ->")
lbl4.grid(row=1, column=0)
last_name = StringVar()
ln = Entry(textvariable=last_name)
ln.grid(row=1, column=1, pady=yval)

#Gender
lbl5 = Label(window, text = "Gender ->")
lbl5.grid(row=2, column=0)
gen = StringVar()
g = Entry(textvariable=gen)
g.grid(row=2, column=1, pady=yval)

#Age
lbl6 = Label(window, text = "Enter Age ->")
lbl6.grid(row=3, column=0)
age = StringVar()
a = Entry(textvariable=age)
a.grid(row=3, column=1, pady=yval)

#Debt
lbl7 = Label(window, text = "Enter Debt ->")
lbl7.grid(row=4, column=0)
debt = StringVar()
d = Entry(textvariable=debt)
d.grid(row=4, column=1, pady=yval)

#Marriage
lbl8 = Label(window, text = "Enter Marital Status ->")
lbl8.grid(row=5, column=0)
mar = StringVar()
m = Entry(textvariable=mar)
m.grid(row=5, column=1, pady=yval)

#Bank Customer
lbl9 = Label(window, text = "Do you have a bank account? ->")
lbl9.grid(row=6, column=0)
bc = StringVar()
b = Entry(textvariable=bc)
b.grid(row=6, column=1, pady=yval)

#Educational Level
lbl10 = Label(window, text = "Enter Education Level ->")
lbl10.grid(row=7, column=0)
el = StringVar()
el = Entry(textvariable=el)
el.grid(row=7, column=1, pady=yval)

#Ethnicity
lbl11 = Label(window, text = "Enter Ethnicity ->")
lbl11.grid(row=8, column=0)
eth = StringVar()
et = Entry(textvariable=eth)
et.grid(row=8, column=1, pady=yval)

#Years Employed
lbl12 = Label(window, text = "Enter number of years employed ->")
lbl12.grid(row=9, column=0)
ye = StringVar()
y = Entry(textvariable=ye)
y.grid(row=9, column=1, pady=yval)

#Prior Default
lbl13 = Label(window, text = "Enter Prior Default ->")
lbl13.grid(row=10, column=0)
pd = StringVar()
p = Entry(textvariable=pd)
p.grid(row=10, column=1, pady=yval)

#Employment status
lbl14 = Label(window, text = "Enter your Employment Status ->")
lbl14.grid(row=11, column=0)
es = StringVar()
e = Entry(textvariable=es)
e.grid(row=11, column=1, pady=yval)

#Credit Score
lbl15 = Label(window, text = "Enter your Credit Score ->")
lbl15.grid(row=12, column=0)
cs = StringVar()
c = Entry(textvariable=cs)
c.grid(row=12, column=1, pady=yval)

#Driver's License
lbl16 = Label(window, text = "Do you have a Driver's License? ->")
lbl16.grid(row=13, column=0)
dl = StringVar()
dri = Entry(textvariable=dl)
dri.grid(row=13, column=1, pady=yval)

#Citizen
lbl17 = Label(window, text = "Are you citizen of the US? ->")
lbl17.grid(row=14, column=0)
citi = StringVar()
cit = Entry(textvariable=citi)
cit.grid(row=14, column=1, pady=yval)

#Zip Code
lbl18 = Label(window, text = "Enter your Zip Code ->")
lbl18.grid(row=15, column=0)
zipc = StringVar()
zip = Entry(textvariable=zipc)
zip.grid(row=15, column=1, pady=yval)

#Income
lbl19 = Label(window, text = "Enter your Income ->")
lbl19.grid(row=16, column=0)
inco = StringVar()
inc = Entry(textvariable=inco)
inc.grid(row=16, column=1, pady=yval)

def app():
    y.get()
    p.get()
    e.get()
    c.get()
    
    lbl = Label(window, text="Hello {0}, your credit card application is {1}".format(fn.get(), answer), bg = 'lightgreen')
    lbl.grid(row=19, column=0, pady=10)

def auto():
    if not g.get():
        g.insert(5, random.choice(['a','b']))

    if not a.get():
        a.insert(5, float("{0:.2f}".format(random.uniform(13.75, 76.75))))

    if not d.get():
        d.insert(5, float("{0:.2f}".format(random.uniform(0., 28.))))

    if not m.get():
        m.insert(5, random.choice(['u','y','l']))

    if not b.get():
        b.insert(5, random.choice(['g','p']))

    if not el.get():
        el.insert(5, random.choice(['c','d','I','j','k','m','r','q','w','x','e','aa','ff']))

    if not et.get():
        et.insert(5, random.choice(['v','h','bb','j','n','z','dd','ff','o']))

    if not y.get():
        y.insert(5, float("{0:.2f}".format(random.uniform(0.0, 28.5))))

    if not p.get():
        p.insert(5, random.choice(['t','f']))

    if not e.get():
        e.insert(5, random.choice(['t','f']))

    if not c.get():
        c.insert(5, float("{0:.2f}".format(random.uniform(0., 68.))))

    if not dri.get():
        dri.insert(5, random.choice(['t','f']))

    if not cit.get():
        cit.insert(5, random.choice(['g','p','s']))

    if not zip.get():
        zipzip = random.choice([0, 17, 45, 49, 50, 52, 56, 60, 62, 110, 112, 117, 120, 121, 156, 160, 163, 164, 167, 168, 170, 171, 220, 221, 224, 225, 228, 230, 231, 232, 239, 240, 250, 252, 253, 254, 260, 268, 340, 348, 349, 350, 352, 408, 410, 416, 420, 422, 431, 432, 434, 440, 443, 450, 454, 455, 460, 465, 470, 480, 711, 720, 760, 840, 980, 2000])
        zip.insert(5, f'{zipzip:05}')

    if not inc.get():
        inc.insert(5, float("{0:.2f}".format(random.uniform(0., 2000.))))


#Apply button
btn = Button(window, text="Apply", command=app, background = 'lightblue')
btn.grid(row=18, column=1, pady=10)

#Auto-fill button
btn = Button(window, text="Auto-fill", command=auto, background = 'lightblue')
btn.grid(row=18, column=2, pady=10)

window.mainloop()
