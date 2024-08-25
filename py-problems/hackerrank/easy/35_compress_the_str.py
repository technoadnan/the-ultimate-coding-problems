from itertools import groupby
ask = input("")
a = [(len(list(g)),int(k)) for k,g in groupby(ask)]
for j in a: print(j,end=" ")
