x = 123

m = x; rev_num = 0
while (m > 0):
   d = m % 10
   rev_num = (rev_num * 10) + d
   m = m // 10 # truncate operation
print(rev_num)