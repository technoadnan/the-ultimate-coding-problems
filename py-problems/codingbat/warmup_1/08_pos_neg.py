def pos_neg(a, b, negative):
   status = False
   if negative == True:
      if (a * -1 == abs(a)) and (b * -1 == abs(b)):
         status = False
   else:
      if (a * -1 != abs(a)) and (b * -1 == abs(b)):
         status = True
      elif (b * 1 == abs(a)) and (b * -1 != abs(b)):
         status = True
   return status 
      
