quantity = int(input(""))
elements = input("").split(" ")
e = []
for j in elements: e.append(int(j))

print(hash(tuple(e)))

