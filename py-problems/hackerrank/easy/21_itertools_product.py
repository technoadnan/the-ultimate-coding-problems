# Enter your code here. Read input from STDIN. Print output to STDOUT
first_row = list(input("").split(" "))
second_row = list(input("").split(" "))

upt_l = []
for i in range(len(first_row)):
   for j in range(len(second_row)):
      upt_l.append((int(first_row[i]),int(second_row[j])))

st = ""
for j in upt_l:
   st = st + str(j) + " "
print(st)