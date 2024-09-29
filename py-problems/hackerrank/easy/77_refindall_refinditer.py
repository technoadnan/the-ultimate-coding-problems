import re
string = input("")
a = re.findall(r"(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])",string=string)

if len(a) >0:
   for j in a:
      print(j)
else:
   print(-1)
# for j in a:
#    print(j)
   # if len(a):
   #    print(-1)
   # print(j)