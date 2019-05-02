import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')
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


def showBoxPlot(x):
    '''
    :param x: list of integers OX
    :return: none
    '''
    x = list(map(float, x))
    x.sort()
    plt.boxplot(x)
    plt.show()


def showScatterPlot(x, y):
    '''
    :param x: list of integers OX
    :param y: list of integers OY
    :return: none
    '''
    x = list(map(float, x))
    y = list(map(float, y))
    x.sort()
    y.sort()
    plt.scatter(x, y)
    plt.show()


def showBarPlot(x):
    '''
    :param x: list of integers OX
    :return: none
    '''
    x = list(map(float, x))
    x.sort()
    plt.bar(x,height = 1)
    plt.show()


def showPiePlot(x):
    '''
    :param x: list of integers OX
    :return: none
    '''
    x = list(map(float, x))
    x.sort()
    plt.pie(x)
    plt.show()


def showPlot(x, y):
    '''
    :param x: list of integers OX
    :param y: list of integers OY
    :return: none
    '''
    x = list(map(float, x))
    y = list(map(float, y))
    x.sort()
    y.sort()
    plt.plot(x, y)
    plt.show()

