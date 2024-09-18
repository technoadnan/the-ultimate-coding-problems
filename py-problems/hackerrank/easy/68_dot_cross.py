import numpy as np

n = int(input(""))

A = []
B = []
for _ in range(n):
   A.append(list(map(int,input("").split(" "))))
for _ in range(n):
   B.append(list(map(int,input("").split(" "))))

A,B = np.array(A), np.array(B)
print(np.dot(A,B))