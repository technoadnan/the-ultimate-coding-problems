# Output total number of students who have subscriptions to the English or the French newspaper but NOT BOTH.

n = int(input(""))
en = set(map(int,input("").split(" ")))
m = int(input(""))
fr = set(map(int,input("").split(" ")))

both_sub = len(en.symmetric_difference(fr))
print(both_sub)
