import re

for j in range(int(input(""))):
   try:
      pattern = re.compile(input(""))  
      print(True) 
   except re.error:
      print(False)
      