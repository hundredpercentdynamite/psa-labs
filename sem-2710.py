import math

n = 16
a1 = 40
a2 = 42
Sd = 3.5

Se = Sd / math.sqrt(n)

t = math.fabs(a1 - a2) / Se

print(t)
