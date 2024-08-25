from itertools import combinations_with_replacement,combinations

string, number = map(str, input("").split())
combinations_with_replacements = list(combinations_with_replacement(sorted(string), int(number)))
combinationss = list(combinations(sorted(string), int(number)))

all_combo = sorted(set(combinations_with_replacements + combinationss))

for j in all_combo:
   print("".join(j))