test_case = int(input())
for j in range(test_case):
   a,b = set(),set()
   n = int(input())
   a.update(map(int,input().split(" ")))
   m = int(input())
   b.update(map(int,input().split(" ")))
   print(a.issubset(b))
   