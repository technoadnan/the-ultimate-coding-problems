import numpy as np
l = list(map(float, input("").split(" ")))
x = int(input(""))
print(np.polyval(l,x=x))
