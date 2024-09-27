# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input(""))

d = {}

for i in range(n):
   user = input("").split(" ")
   d[user[0]] = user[1]

try:
   while True:
      q = input("")
      if q in d:
         print(f"{q}={d[q]}")
      else:
         print("Not found")
except EOFError:
   pass
