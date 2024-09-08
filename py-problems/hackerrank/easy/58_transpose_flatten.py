import numpy as np

n,m = map(int,input().split(" "))
l = []
for j in range(n):
   l.append(list(map(int,input().split(" "))))
upt_arr = np.array(l)
print(f"{np.transpose(upt_arr)}\n{upt_arr.flatten()}")