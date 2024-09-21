
for j in range(int(input())):
   n = int(input())
   # spilt the datas 
   a = list(map(int,input().split()))
   length = len(a)//2

   left,right = [],[]
   for j in range((length)):
      left.append(a[j])
   for j in range(length,len(a)):
      right.append(a[j])

   l,r = 0,0
   status = "No"
   for j in left:
      if j >= l:
         l = j
      else:
         status = "No"
         break
      status = "Yes"

   for k in right:
      if k >= r:
         r = k
      else:
         # print(False)
         status = "No"
         break
      status = "Yes"

   print(status)