ans = []
for j in range(int(input())):
   try:
      ask = input()
      if ask == '0':
         ans.append(False)
         break
      ans.append(True)  
   except ValueError:
      ans.append(False)

print("\n".join(map(str,ans)))
