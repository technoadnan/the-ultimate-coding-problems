def front_back(str):
   reverse_st = str[1:-1:]
   if len(str) > 1:
      return str[-1:] + reverse_st + str[:1]
   return str