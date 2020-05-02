from math import exp
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
import numpy as np
import os


def func(x, a, b, c):
    # return a * (x ** 3) + b * (x ** 2) + c * x + d + e * (x ** 4) + f * (x ** 5)
    return a * (x ** 2) + b * x + c
    # return a * x + b
    # return abs(a) * (x ** 2) + c
    # return a ** (b*x+c) + d * x + e
    # return  abs(a) * np.exp(c*x+d)+b
    # return a * exp(b * pd.to_numeric(x))+ c
    # return abs(a) * np.log(x)+d
    #return abs(a)*np.exp(b*x)+abs(c)*x+d
    # return abs(a) * (x+d) ** 2 + abs(b) * x + c #+ abs(d) * x ** 3
    # return a * (x ** 3) + b * (x ** 2) + c * x + d + e * (x ** 4)+ f * (x ** 5)
    # return a * (x ** 3) + b * (x ** 2) + c * x + d + e * (x ** 4) + f * (x ** 5)+ g * (x ** 6)


def getMaxX(df):
    return df.max()


def getMinX(df):
    return df.min()


def getMaxY(df):
    return df.max()


def getMinY(df):
    return df.min()


def plotGraph(x, y, queue_name, k, path):

    # Getting parameters for function
    beta_opt, beta_cov = curve_fit(func, x, y)
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    # ax.plot(x, y, 'r', lw=2)
    print(*beta_opt)
    # ax.plot()
    # creating a range of data to plot
    xx = []
    xmin = int(getMinX(x))
    xmax = int(getMaxX(x))
    delta = (xmax - xmin) / 20000 * k
    for i in range(20000):
        xx.append(delta * i)
    xxx = pd.DataFrame(data=xx)
    ax.plot(xxx, func(xxx, *beta_opt), 'b', lw=2, label=queue_name + ' extrapolation')
    plt.legend(loc="upper left")
    ax.set_xlim(xmin, (xmax - xmin) * k)
    ax.set_ylim(getMinY(y), getMaxY(y))
    ax.set_xlabel(r"$x$", fontsize=18)
    ax.set_ylabel(r"$f(x, \beta)$", fontsize=18)
    plt.savefig(path + queue_name.replace('/', '_') + '.png')
    plt.close()


class Analysis:
    @staticmethod
    def plotGraph(df, key):
        print('4/4 Plot Graphs')
        processes = df[1]
        data = df[0]
        path = os.getcwd()+'/result/'
        try:
            os.mkdir(path)
        except OSError:
            print("Creation of the directory %s failed" % path)

        for processName in processes:
            print(processName)
            dat = data.loc[data['Display_Process_Name'] == processName]
            if dat.size < 20:
                print("Not enough data to make a prediction for: " + processName)
            else:
                #plotGraph(dat['getCount_90'], dat['percentile_90'], processName, key, path)
                plotGraph(dat['load'], dat['percentile_90'], processName, key, path)
