string = input()
char,integer = [],[]

for j in string:
   if j.isnumeric():
      integer.append(int(j))
   else:
      char.append(j)

odd = sorted([x for x in integer if x%2==1])
even = sorted([x for x in integer if x%2==0])

lowercase = sorted([x for x in char if x.islower()])
uppercase = sorted([x for x in char if x.isupper()])

integer = odd+even
char = lowercase + uppercase

result = "".join(map(str,char+integer))
print(result)

