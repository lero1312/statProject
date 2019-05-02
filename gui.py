from tkinter import *
from graph import *
from oo import *
from tkinter import messagebox


Data = []
Data2 = []
x = 0
z = 0


top = Tk()

def add():
    for i in E1.get().split():
        Data.append(int(i))

    Var = StringVar()
    Mean=Label(top,textvariable=Var)
    Mean.pack(side=TOP)
    Var.set("Mean: "+str(cMean(Data)))

    V= StringVar()
    Median = Label(top, textvariable=V)
    Median.pack(side=TOP)
    V.set("median: " + str(cMed(Data)))

    V2 = StringVar()
    Mode = Label(top,  textvariable=V2)
    Mode.pack(side=TOP)
    V2.set("Mode: " + str(cMode(Data)))

    q1 = StringVar()
    qq1 = Label(top, textvariable=q1)
    qq1.pack(side=TOP)
    q1.set("Q1 : " + str(Q1(x, Data)))

    q3 = StringVar()
    qq3 = Label(top, textvariable=q3)
    qq3.pack(side=TOP)
    q3.set("Q3 : " + str(Q3(x, z, Data)))

    q2 = StringVar()
    qq2 = Label(top, textvariable=q2)
    qq2.pack(side=TOP)
    q2.set("Q2 : " + str(Q2(x, Data)))

    iq = StringVar()
    IQ = Label(top, textvariable=iq)
    IQ.pack(side=TOP)
    iq.set("IQR : " + str(cIQR(x, Data)))

def fill():
    for i in E1.get().split():
        Data.append(int(i))
    for i in E2.get().split():
        Data2.append(int(i))


def sHist():
    fill()
    showHist(list(Data), list(Data2))


def sBoxPlot():
    fill()
    showBoxPlot(list(Data))


def sScatterPlot():
    fill()
    showScatterPlot(list(Data), list(Data2))


def sBarPlot():
    fill()
    showScatterPlot(list(Data), list(Data2))


def sPiePlot():
    fill()
    showPiePlot(list(Data))
def sPlot():
    fill()
    showPlot(list(Data), list(Data2))


E1 = Entry(top,width=20 ,bd=4)
E1.pack(side=TOP)

E2 = Entry(top,width=20 ,bd=4)
E2.pack(side=TOP)

ss = Button(top, text="show", command=add)
ss.pack(side=TOP)

v1 = Button(top, text="show Histo", command=sHist)
v1.pack(side=TOP)

v2 = Button(top, text="show Box Plot", command=sBoxPlot)
v2.pack(side=TOP)

v3 = Button(top, text="show Scatter Plot", command=sScatterPlot)
v3.pack(side=TOP)

v4 = Button(top, text="show Bar Plot", command=sBarPlot)
v4.pack(side=TOP)

v5 = Button(top, text="show Pie Plot", command=sPiePlot)
v5.pack(side=TOP)

v6 = Button(top, text="show Plot", command=sPlot)
v6.pack(side=TOP)


top.mainloop()
