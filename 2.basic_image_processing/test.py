import numpy as np

a = np.arange(0, 9).reshape(3,3)
b = np.arange(0,9).reshape(3,3)
print(a)
print(b)

print(a*b)
print(a.dot(b))
print((a*b).sum())