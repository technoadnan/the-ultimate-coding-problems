ask = int(input(""))
results = []
for _ in range(ask):
   a,b = map(str,input("").split(" "))
   try:
      division = int(a)//int(b)
      results.append(division)
   except ZeroDivisionError as z:
      results.append(f"Error Code: {z}")
   except ValueError as v:
      results.append(f"Error Code: {v}")

for result in results:
   print(result)