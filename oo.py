import math

def cMed(val):
    if (len(val)%2 != 0):
        return val[int(len(val) / 2)]
    else:
        return (val[int(len(val) / 2)] + val[int(len(val) / 2) - 1]) / 2

def cLargstOutlier(m, val):
    q3 = Q3(m, int(m / 2), val)
    iqr = cIQR(m, val)
    return q3 + 1.5*iqr



def cLenInterval(val, z):
    lengthOfInterval = int((val[len(val) - 1] - val[0]) / z)
    if (val[len(val) - 1] - val[0])%z != 0 :
        lengthOfInterval+=1
    return lengthOfInterval



def cMean(values):
    Mean = 0
    for i in values:
        Mean += i
    Mean /= len(values)
    return Mean



def cIQR(m, val):
    return Q3(m, int(m / 2), val) - Q1(int(m / 2) - 1, val)


def cNoIntervals(values):
    z = int(math.log(len(values), 2) + 2)
    return z




def cMode(val):
    C = 0
    MAX = 0
    mode = 0
    F = {}
    for i in val:
        if (i in F):
            F[i] += 1
        else:
            F[i]=1
        MAX = max(MAX , F[i])

    for key , val in F.items():
        if val==MAX:
            C += 1
            mode = key

    if C > 1:
        return  -1
    return  mode




def Q2(m, val):
    if (m%2 != 0):
        return val[int(m / 2)]
    else:
        return (val[int(m / 2)] + val[int(m / 2) - 1]) / 2



def Q1(m, val):
    if (m%2 == 0):
        return val[int(m / 2)]
    else:
        return (val[int(m / 2)] + val[int(m / 2) + 1]) / 2


def Q3(m, m2, val):
    if (m%2 != 0):
        m2 += 1

    if ((m - m2)%2 != 0):
        return  val[int((m + m2) / 2)]
    else:
        return (val[int((m + m2 - 1) / 2)] + val[int((m + m2 - 1) / 2) + 1]) / 2




def cSmlstOutlier(m, val):
    q1 = Q1(int(m / 2) - 1, val)
    iqr = cIQR(m, val)
    return q1 - 1.5*iqr
