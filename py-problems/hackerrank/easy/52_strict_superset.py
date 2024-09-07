# s = {1,3,4}
# a = {1,4}
# # k = a.difference(s)
# # print(k)

s = set(map(int,input("").split()))
n = int(input())
ss = set()
status = False
for j in range(n):
   l = list(map(int,input().split()))
   for i in l:
      if i not in s:
         status = False
         break
      else:
         status = True
      
print(status)
