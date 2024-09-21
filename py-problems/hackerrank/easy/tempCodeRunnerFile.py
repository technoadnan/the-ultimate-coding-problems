import numpy as np

n = int(input(""))

array = []

for j in range(n):
   l = list(map(float, input("").split(" ")))
   print(l)
   array.append(l)

array = np.array(array)

print(np.linalg.det(array))

