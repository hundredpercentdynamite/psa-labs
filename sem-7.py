import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf



exp = [1, 0, 0, 1, 0, 0, 0, 0, 1, 1]

pCount = 0

for j in exp:
    if (j == 1):
        pCount += 1

expLen = len(exp)
p1 = pCount / expLen
q = 1 - p1

odd = p1 / q
print("Odd", odd)

# part 2

pos = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
neg = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

ps = pos / (len(pos) - 1)
odds = []
for p in ps:
    if (1 - p) == 0:
        odds.append(1)
    else:
        odds.append(p / (1 - p))

logs = np.log(odds)
logOdd = math.log(odd)
plot = plt.scatter(logs[0:-1], ps[0:-1])
plt.scatter([logOdd], [p1])
plt.show()

# часть 3
df = pd.read_csv('Titanic.csv')
df = df[df.Age.notnull()]
glm_binominal = smf.glm(formula="Survived ~ 1", data=df, family=sm.families.Binomial()).fit()
print(glm_binominal.summary())
print(glm_binominal.aic)

ppp = math.exp(-0.3799) / (math.exp(-0.3799) + 1)
print("P: ", ppp)

sns.countplot(x='Survived', data=df, palette='hls')
