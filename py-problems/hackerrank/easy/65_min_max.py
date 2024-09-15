import numpy as np

n,m = map(int,input("").split(" "))

l = []
for _ in range(n):
   l.append(list(map(int,input("").split(" ")))) 

array = np.array(l)
min_l = max(np.min(array,axis=1))
print(min_l)