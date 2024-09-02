from collections import deque

d = deque()

for j in range(int(input(""))):
   info = input().split(" ")
   operation = info[0]
   a = getattr(d,operation)
   if len(info) == 2:
      num = int(info[1])
      a(num)
   else:
      a()


print(' '.join(map(str, map(int, d))))