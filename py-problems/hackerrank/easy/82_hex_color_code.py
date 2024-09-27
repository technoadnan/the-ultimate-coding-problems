import re

string = ""

for j in range(int(input(""))):
    query = input("")
    string = string + query
    

search = r"(#[0-9a-fA-F]{3}|#[0-9a-fA-F]{6})(?=[;),])"
a = re.findall(search, string)
for j in a:print(j)