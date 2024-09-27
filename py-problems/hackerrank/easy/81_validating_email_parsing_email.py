import re
import email.utils
search = r"^[a-zA-Z][\w.-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$"


for j in range(int(input(""))):
   name,email_address = email.utils.parseaddr(input())
   # a = re.match(search,query[1])
   if re.match(search,email_address):
      print(f"{name} <{email_address}>")