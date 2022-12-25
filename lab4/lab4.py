import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf

# PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked

df = pd.read_csv('Titanic.csv')
df = df[df.Age.notnull()]
glm_binominal = smf.glm(formula="Survived ~ Pclass + Sex + Age + Fare", data=df,
                        family=sm.families.Binomial()).fit()
print(glm_binominal.summary())
print("AIC :", glm_binominal.aic)


sns.countplot(x='Sex', data=df, palette='hls')
plt.show()

sns.countplot(x='Pclass', data=df, palette='hls')
plt.show()

sns.boxplot(x='Survived', y='Age', data=df)
plt.show()

sns.boxplot(x='Survived', y='SibSp', data=df)
plt.show()

sns.boxplot(x='Survived', y='Parch', data=df)
plt.show()

sns.boxplot(x='Survived', y='Fare', data=df)
plt.show()

sns.displot(x='Age', data=df)
plt.show()

sns.displot(x='SibSp', data=df)
plt.show()

sns.displot(x='Parch', data=df)
plt.show()

sns.displot(x='Fare', data=df)
plt.show()

cols = ["Age", "SibSp", "Parch", "Fare"]
corr = df[cols].corr()

sns.heatmap(corr, annot=True)
plt.show()
