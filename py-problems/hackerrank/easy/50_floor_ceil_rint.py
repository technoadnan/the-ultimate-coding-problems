import numpy as np

l = list(map(float,input().split(" ")))
array = np.array(l)

np.set_printoptions(legacy='1.13')

print(np.floor(array))
print(np.ceil(array))
print(np.rint(array))