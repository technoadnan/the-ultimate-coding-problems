from itertools import combinations
from collections import Counter
n = int(input())
string = input().split(" ")
k = int(input())

string.insert(0,None) # making it 1 index
target_word = "a"
indicies = [i for i, x in enumerate(string) if x == target_word]

probability = list(combinations(range(1, n + 1), k))

# print(probability)
counter = 0
for j in probability:
   if any(index in indicies for index in j):
      counter += 1

print(f"{counter/len(probability)}")



