# s = set(map(int, input().split()))

s =  set()

n = int(input(""))
elements = list(map(int, input("").split(" ")))
operations_n = int(input(""))
s.update(elements)

print(s) 
for _ in range(operations_n):
   operations_user = (input("").strip().split(" "))
   operation = operations_user[0]
   try:
      num = int(operations_user[1])
   except IndexError:
      pass
   if operation == "pop":
      s.pop()
   if operation == "remove" or operation == "discard":
      s.discard(num)

print(sum(s))
