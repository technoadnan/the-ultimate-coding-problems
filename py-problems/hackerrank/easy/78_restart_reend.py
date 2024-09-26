import re
# string = ""
string = input("")
matching = input("")
matches = list(re.finditer(f'(?={matching})', string))
if not matches:
   print((-1,-1))
else:
   for j in matches:
      # print(j)
      print((j.start(),j.start()+len(matching)-1))