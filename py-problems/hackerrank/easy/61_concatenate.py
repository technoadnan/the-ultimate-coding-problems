# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

n,m,p = map(int,input().split(" "))
array_1 = np.array([input().split() for _ in range(n)], int)
array_2 = np.array([input().split() for _ in range(m)], int)
result = np.concatenate((array_1, array_2), axis=0)
print(result)