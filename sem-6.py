import numpy as np
import math

def getCorelLong(xs, ys):
    n = len(xs)
    sumNum = 0
    sumX = 0
    sumY = 0
    avgX = np.average(xs)
    avgY = np.average(ys)
    for i in range(0, n):
        a = xs[i] - avgX
        b = ys[i] - avgY
        sumNum += a * b
        sumX += pow(a, 2)
        sumY += pow(b, 2)
    return sumNum / (math.sqrt(sumX) * math.sqrt(sumY))

def task1():
    print("Задача 1")
    x = np.array([2, 4, 1, 7, 3, 11, 14, 15, 21, 4])
    y = np.array([7, 6, 4, 11, 2, 21, 31, 23, 40, 15])

    print("r_xy: ", getCorelLong(x, y))

task1()


def corelEstimation(data):
    k = len(data)
    ni = 3
    n = k * ni
    numSum = 0
    denumSum = 0
    avgX = 0

    for [yi, xij] in data:
        avgXi = np.average(xij)
        avgX += avgXi / k

    for [yi, xij] in data:
        avgXi = np.average(xij)
        a = 3 * pow(avgXi, 2)
        numSum += a
        xSum = 0
        for x in xij:
            xSum += pow(x, 2)
        denumSum += xSum
    return (numSum - (n * pow(avgX, 2))) / (denumSum - (n * pow(avgX, 2)))

def getL(nu, n, k):
    num = nu * (n - k)
    denum = (k - 1) * (1 - nu)
    return num / denum

def task2():
    print()
    print()
    print("Задача 2")
    table = np.array([
        [2, [1, 3, 4]],
        [4, [7, 8, 12]],
        [9, [14, 19, 21]],
        [13, [11, 9, 6]],
        [15, [8, 7, 3]]
    ])

    estimation = corelEstimation(table)
    l = getL(estimation, 15, 5)
    F = 3.48
    f1 = 5 - 1
    f2 = 15 - 5
    print("Nu^2:", estimation)
    print("l:", l)
    print("Степени свободы: ", f1, "и", f2)
    print("Табличное значение F_0.95(4, 10):", F)
    print("H0:", "Случайные величины Х и Y не имеют корреляции")
    if (l > F):
        print("Нулевая гипотеза отклоняется с достоверностью 0.95, так как F_0.95(4, 10) < l")

task2()


