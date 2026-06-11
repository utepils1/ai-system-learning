import numpy as np

# 标量
scalar = np.array(5)

# 向量
vector = np.array([1, 2, 3])

# 矩阵
matrix = np.array([
    [1, 2],
    [3, 4]
])

# 三维张量
tensor = np.array([
    [[1, 2],
     [3, 4]],

    [[5, 6],
     [7, 8]]
])

print("scalar shape:")
print(scalar.shape)

print("\nvector shape:")
print(vector.shape)

print("\nmatrix shape:")
print(matrix.shape)

print("\ntensor shape:")
print(tensor.shape)