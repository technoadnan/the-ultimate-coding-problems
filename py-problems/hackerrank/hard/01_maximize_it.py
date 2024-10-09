

from itertools import product

# Function to generate combinations using *args
def generate_combinations(*args):
   return product(*args)

num_lines = input("").split(" ")

lines = []

for _ in range(int(num_lines[0])):
   l = list(map(int,input().split()))[1:]
   lines.append(l)
combinations = product(*lines)

max_num = []
for comb in combinations:
   sq = (*map(lambda x:x**2, comb),) # explain
   max_num.append(sum(sq)%int(num_lines[1]))
print(max(max_num))
