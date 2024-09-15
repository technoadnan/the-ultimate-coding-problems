import numpy as np

n,m = map(int,input("").split(" "))

l = []
for _ in range(n):
   l.append(list(map(int,input("").split(" "))))

array = np.array(l)
print(np.mean(array,axis=1))
print(np.var(array,axis=0))
print((round(np.std(array,axis=None),ndigits=11)))
