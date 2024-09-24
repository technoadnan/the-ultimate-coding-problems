# n = int(input(""))
# # even,odd=[],[]
# even,odd = "",""

# for j in range(n):
#    user = input()
#    for i in range(len(user)):
#       if i % 2 == 0:
#          even += user[i]
#       else:
#          odd += user[i]
   
#    even += " "
#    odd += " "
# even = even.split(" ")
# odd = odd.split(" ")
# for j in range(n):
#    print(even[j]+ " "+odd[j])

## easy way to do 

n = int(input(""))
ans = ""
for j in range((n)):
   user = input("")
   even = user[::2]
   odd = user[1::2]
   ans = ans + f"{even} {odd}" + "\n"

print(ans.rstrip('\n'))

