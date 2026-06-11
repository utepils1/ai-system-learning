import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print("原数组:")
print(a)

print("\n原 shape:")
print(a.shape)

print("\nreshape(2, 4):")
print(a.reshape(2, 4))

print("\nreshape(4, 2):")
print(a.reshape(4, 2))

print("\nreshape(2, 2, 2):")
print(a.reshape(2, 2, 2))

print("\nreshape(2, -1):")
print(a.reshape(2, -1))

print("\nreshape(-1, 2):")
print(a.reshape(-1, 2))