n = int(input(""))
en = set(map(int,input("").split(" ")))
m = int(input(""))
fr = set(map(int,input("").split(" ")))

both_sub = len(en.intersection(fr))
print(both_sub)