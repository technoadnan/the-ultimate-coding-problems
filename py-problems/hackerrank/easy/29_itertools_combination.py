from itertools import combinations

string, number = map(str, input("").split())
string = ''.join(sorted(string))  # sort the string
for i in range(1, int(number) + 1):
   all_permutations = list(combinations(string, i))
   for j in all_permutations:
      str_format = ''.join(j)
      print(str_format)