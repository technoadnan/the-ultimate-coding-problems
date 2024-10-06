
import re
main_regex = r"[456](?!.*(.)\1{3})(?!.* )[0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}$"
check_dash = r"^\d{4}-?\d{4}-?\d{4}-?\d{4}$"


for j in range(int(input())):
   query = input("")
   flat_num = "".join("".join(map(str,re.findall(check_dash,query))).split("-"))
   if flat_num:

      if re.match(main_regex,flat_num):
         print("Valid")
      else:
         print("Invalid")
   else:
      print("Invalid")
