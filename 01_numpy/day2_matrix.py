import numpy as np

a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

print("矩阵A:")
print(a)

print("\n矩阵B:")
print(b)

print("\n矩阵加法:")
print(a + b)

print("\n矩阵乘法:")
print(a @ b)