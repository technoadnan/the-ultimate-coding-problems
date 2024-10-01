import re


all_code = ""
for _ in range(int(input(""))):
   code = input("")
   code = re.sub(r"(?<= )&&(?= )","and",code,flags=re.MULTILINE)
   code = re.sub(r"(?<= )\|\|(?= )","or",code,flags=re.MULTILINE)
   all_code = all_code  + code + "\n"

print(all_code)