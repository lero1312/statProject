#import numpy as np; np.random.seed(13)
import matplotlib.pyplot as plt
import math
matplotlib.style.use('ggplot')


def calNumOfIntervals(values):
    k = int(math.log(len(values),2)+2)
    return k



def calcLengthOfInterval(values,k):
    lenOfInterval = int((values[len(values)-1]-values[0])/k)
    if (values[len(values)-1]-values[0])%k != 0 :
        lenOfInterval+=1
    return lenOfInterval



def calcMean(values):
    mean = 0
    for i in values:
        mean += i
    mean /= len(values)
    return mean


values = [int(i) for i in input().split()]
numOfData = len(values)
values.sort()

#Calculate IQR
def calcIQR(n , values):
    return calcQ3(n , int(n/2) , values) - calcQ1(int(n/2)-1 , values)


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



