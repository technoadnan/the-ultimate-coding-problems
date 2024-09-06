# s = {1,3,4}
# a = {1,4}
# # k = a.difference(s)
# # print(k)

s = set(map(int,input("").split()))
n = int(input())
ss = set()
for j in range(n):
   ss.update(map(str,input().split()))

if ss.difference(s):
   print(False)
else:
   print(True)
# print(ss)
# print(s)