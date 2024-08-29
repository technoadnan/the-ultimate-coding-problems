from collections import namedtuple

n, Info= int(input("")), namedtuple('Info',input("").split())

total = 0
for _ in range(n):
   data = input().split()
   record = Info(*data)
   total += int(record.MARKS)

print(f"{(total/n):.2f}")

# solution in 4 line
# from collections import namedtuple
# n, Info= int(input("")), namedtuple('Info',input("").split())
# total = sum(int(Info(*input().split()).MARKS) for _ in range(n))
# print(f"{(total/n):.2f}")