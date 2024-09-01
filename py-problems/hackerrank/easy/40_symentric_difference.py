n = int(input(""))
set_a = set(map(int,input("").split(" ")))
m = int(input(""))
set_b = set(map(int,input("").split(" ")))

not_b = set_a.difference(set_b)
not_a = set_b.difference(set_a)

symmetric_diff = sorted(not_a | not_b)
print(symmetric_diff)

print(" \n".join(map(str,symmetric_diff)))