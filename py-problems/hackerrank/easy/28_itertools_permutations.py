from itertools import permutations

string, number = map(str, input("").split())
all_permutations = list(sorted(permutations(string, int(number))))
for j in all_permutations:
   str_format = ''.join(j)
   print(str_format)