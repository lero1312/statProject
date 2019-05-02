from tkinter import *
import matplotlib.pyplot as plt
import math
from graph import *
from number import *


from tkinter import messagebox

from numpy.ma import var

top = Tk()

Data=[1,2,3,4,5,6]
#list=[1,2,3,4,5,6]
Data=[]

x=0
z=0




def add():
    for i in E1.get().split():
        Data.append(int(i))
        print(len(Data))


    Var = StringVar()
    Mean=Label(top,textvariable=Var)
    Mean.pack(side=TOP)
    Var.set("Mean: "+str(cMean(Data)))

    V= StringVar()
    Median = Label(top, textvariable=V)
    Median.pack(side=TOP)
    V.set("median: " + str(cMed(Data)))

    V2 = StringVar()
    Mode= Label(top,  textvariable=V2)
    Mode.pack(side=TOP)
    V2.set("Mode: " + str(cMode(Data)))

    q1 = StringVar()
    Q1 = Label(top, textvariable=q1)
    Q1.pack(side=TOP)
    q1.set("Q1 : " + str(Q1(x, Data)))

    q3 = StringVar()
    Q3 = Label(top, textvariable=q3)
    Q3.pack(side=TOP)
    q3.set("Q3 : " + str(Q3(x, z, Data)))


    q2 = StringVar()
    Q2 = Label(top, textvariable=q2)
    Q2.pack(side=TOP)
    q2.set("Q2 : " + str(Q2(x, Data)))

    iq = StringVar()
    IQ = Label(top, textvariable=iq)
    IQ.pack(side=TOP)
    iq.set("IQR : " + str(cIQR(x, Data)))

    showBoxPlot(Data)



add = Button(top, text="Add", command=add)
add.pack(side=TOP)




E1 = Entry(top,width=20 ,bd=4)
E1.pack(side=TOP)



top.mainloop()
