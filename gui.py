from tkinter import *
 #import numpy as np; np.random.seed(13)
import matplotlib.pyplot as plt
import math


from tkinter import messagebox

from numpy.ma import var

top = Tk()

Data=[1,2,3,4,5,6]
#list=[1,2,3,4,5,6]
Data=[]

x=0
z=0

def calcMean(values):
    mean = 0
    for i in values:
        mean += i
    mean /= len(values)
    return mean
def calcMedian(values):
    if (len(values)%2 != 0):
        return values[int(len(values)/2)]
    else:
        return (values[int(len(values)/2)] + values[int(len(values)/2)-1])/2



def calcMode(val):
    freq = {}
    mx = 0
    cnt = 0
    mode = 0
    for i in val:
        if (i in freq):
            freq[i] += 1
        else:
            freq[i]=1
        mx = max(mx , freq[i])

    for key , val in freq.items():
        if val==mx:
            cnt += 1
            mode = key

    if cnt > 1:
        return  -1
    return  mode
def calNumOfIntervals(values):
    k = int(math.log(len(values),2)+2)
    return k



def calcLengthOfInterval(values,k):
    lenOfInterval = int((values[len(values)-1]-values[0])/k)
    if (values[len(values)-1]-values[0])%k != 0 :
        lenOfInterval+=1
    return lenOfInterval

def calcIQR(n , values):
    return calcQ3(n , int(n/2) , values) - calcQ1(int(n/2)-1 , values)


#Calculate Smalest Out liers
def calcSmallestOutliers(n , values):
    q1 = calcQ1(int(n/2)-1 , values)
    IQR = calcIQR(n , values)
    return q1 - 1.5*IQR

def calcQ2(n , values):
    if (n%2 != 0):
        return values[int(n/2)]
    else:
        return (values[int(n/2)] + values[int(n/2)-1])/2



def calcQ1(n , values):
    if (n%2 == 0):
        return values[int(n/2)]
    else:
        return  (values[int(n/2)] + values[int(n/2)+1])/2


def calcQ3(n , n2 , values):
    if (n%2 != 0):
        n2 += 1

    if ((n-n2)%2 != 0):
        return  values[int((n+n2)/2)]
    else:
        return (values[int((n+n2-1)/2)] + values[int((n+n2-1)/2)+1])/2



#Calculate Largest Out liers
def calcLargestOutliers(n , values):
    q3 = calcQ3(n , int(n/2) , values)
    IQR = calcIQR(n, values)
    return q3 + 1.5*IQR



def showBoxPlot(x):
    '''
    :param x: list of integers OX
    :return: none
    '''
    x = list(map(float, x))
    x.sort()
    plt.boxplot(x)
    plt.show()
def showHist(x, y):
    '''
    :param x: list of integers OX
    :param y: list of integers OY
    :return: none
    '''
    x = list(map(float,x))
    y = list(map(float,y))
    x.sort()
    y.sort()
    plt.hist(x,y,rwidth=0.9)
    plt.show()



def add():
    for i in E1.get().split():
        Data.append(int(i))
        print(len(Data))


    Var = StringVar()
    Mean=Label(top,textvariable=Var)
    Mean.pack(side=TOP)
    Var.set("Mean: "+str(calcMean(Data)))

    V= StringVar()
    Median = Label(top, textvariable=V)
    Median.pack(side=TOP)
    V.set("median: "+str(calcMedian(Data)))

    V2 = StringVar()
    Mode= Label(top,  textvariable=V2)
    Mode.pack(side=TOP)
    V2.set("Mode: "+str(calcMode(Data)))

    q1 = StringVar()
    Q1 = Label(top, textvariable=q1)
    Q1.pack(side=TOP)
    q1.set("Q1 : " + str(calcQ1(x, Data)))

    q3 = StringVar()
    Q3 = Label(top, textvariable=q3)
    Q3.pack(side=TOP)
    q3.set("Q3 : " + str(calcQ3(x,z, Data)))


    q2 = StringVar()
    Q2 = Label(top, textvariable=q2)
    Q2.pack(side=TOP)
    q2.set("Q2 : " + str(calcQ2(x,Data)))

    iq = StringVar()
    IQ = Label(top, textvariable=iq)
    IQ.pack(side=TOP)
    iq.set("IQR : " + str(calcIQR(x, Data)))

    showBoxPlot(Data)



add = Button(top, text="Add", command=add)
add.pack(side=TOP)




E1 = Entry(top,width=20 ,bd=4)
E1.pack(side=TOP)



top.mainloop()
