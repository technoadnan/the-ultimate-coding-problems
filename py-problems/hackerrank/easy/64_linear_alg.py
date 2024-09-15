import numpy as np

n = int(input(""))

array = []

for j in range(n):
   l = list(map(float, input("").split(" ")))
   array.append(l)

array = np.array(array)

print(round(np.linalg.det(array),ndigits=2))


