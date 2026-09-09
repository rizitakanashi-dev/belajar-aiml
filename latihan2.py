import numpy as np

matriks = np.array([
    [80, 85],
    [90, 75],
    [60, 95]
])

print("nilai bahasa inggris:", matriks[:, 1])

print("rata-rata nilai mtk:", np.mean(matriks[:, 0]))

