from itertools import combinations_with_replacement

string, number = map(str, input("").split())
all_permutations = list(sorted(combinations_with_replacement(string, int(number))))

for j in all_permutations:
   str_format = ''.join(j)
   print(str_format)