from collections import Counter
numbers = list(map(int,input("").strip().split(" ")))
a = Counter(numbers)

for k,v in a.items():
   if v == 1: # we know that the captain room is only one
      print(k)
   