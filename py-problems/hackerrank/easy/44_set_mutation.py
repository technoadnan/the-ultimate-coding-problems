n = int(input())
numbers = set(map(int,input("").split(" ")))
# print(numbers)
for j in range(int(input(""))):
   info = input().split(" ")
   operation= getattr(numbers,info[0]) # parameter: 1-> operation want to perform 2-> operation name
   m = set(map(int,input().split(" ")))
   operation(m)

print(sum(numbers))
