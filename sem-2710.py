import math

def task1():
    n = 16
    a1 = 40
    a2 = 42
    Sd = 3.5

    Se = Sd / math.sqrt(n)

    t = math.fabs(a1 - a2) / Se

    print(t)

def task2():
    n = 50
    a1 = 1282
    s1 = 80
    d1 = s1**2

    a2 = 1208
    s2 = 94
    d2 = s2**2

    z = (a1 - a2) * math.pow(((d1 / n) + (d2 / n)), -0.5)
    print("z = ", z)

task2()
