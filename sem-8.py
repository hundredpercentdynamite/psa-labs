import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

dots = np.array([
    [2,	5],
    [7,	10],
    [1,	1],
    [9,	3],
    [5,	6],
    [5,	9],
    [2,	8],
    [6,	10],
    [1,	7],
    [8,	8]
])

# plt.scatter(dots[:,0], dots[:,1], label="Position")

# plt.show()
kmeans = KMeans(n_clusters=2)
kmeans.fit(dots)

centers = kmeans.cluster_centers_
print(centers)

excel_results = np.array([
    [1.5, 4.75],
    [5.5, 6],
])

plt.scatter(dots[:,0], dots[:,1], c=kmeans.labels_, cmap='rainbow')

# plt.show()

# Зелёные - результат расчёта из библиотеки
plt.scatter(centers[:,0], centers[:,1], edgecolors="green")
# Жёлтые - результат расчёта из эксель
plt.scatter(excel_results[:,0], excel_results[:,1], edgecolors="yellow")
plt.xlim(0, 11)
plt.ylim(0, 11)
plt.show()
