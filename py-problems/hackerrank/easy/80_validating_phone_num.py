# Enter your code here. Read input from STDIN. Print output to STDOUT


import re
for j in range(int(input(""))):
   query = input("")
   a = re.findall(r"^[6-9]\d{9}$",query)
   if a:
      print("YES")
   else:
      print("NO")
