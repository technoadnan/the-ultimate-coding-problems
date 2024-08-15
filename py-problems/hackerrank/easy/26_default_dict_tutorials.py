from collections import defaultdict

all_dict = defaultdict(list)
n,m = map(int, input("").split())

indexes = defaultdict(list)
final_indexes = []

for j in range(n):
   ask = input("")
   indexes[ask].append(j+1) # puts letter and index together

for _ in range(m):
   ask = input("")
   if ask in indexes:
      final_indexes.append(" ".join(map(str, indexes[ask]))) # map -> int to str 
   else:
      final_indexes.append(-1)

for result in final_indexes:
   print(result)

