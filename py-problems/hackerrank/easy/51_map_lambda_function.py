# sum = lambda a,b,c: a+b+c
# print(sum(1,2,3))

# i,j = 0,1
# l = []
# n = int(input())
# for _ in range(n-2):
#    k = i + j
#    i=j
#    j=k
#    l.append(pow(k,3))
# l.insert(0,0)
# l.insert(1,1)
# print(l)


cube = lambda x: pow(x,3)

def fibonacci(n):
   # return a list of fibonacci numbers
   i,j = 0,1
   l = []
   for _ in range(n-2):
      k = i + j
      i=j
      j=k
      l.append(k)
   if n >= 2 or n == 1:
      l.insert(0,0)
   if n >= 2 or n == 2:
      l.insert(1,1)
   return l

if __name__ == '__main__':
   n = int(input())
   print(list(map(cube, fibonacci(n))))