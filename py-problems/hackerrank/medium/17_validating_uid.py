import re

query = int(input(""))


def check(j):
   if len(j) != 10 or len(set(j)) != 10:
      return "Invalid"
   if len(re.findall(r"[A-Z]",j)) < 2:
      return "Invalid"
   if len(re.findall(r"\d",j)) < 3:
      return "Invalid"
   if not j.isalnum():
      return "Invalid"
   return "Valid"



for _ in range(query):
   uid_user = input("")
   print(check(uid_user))