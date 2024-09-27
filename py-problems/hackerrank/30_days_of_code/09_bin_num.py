import math
import os
import random
import re
import sys
from collections import Counter
import re

if __name__ == '__main__':
   n = int(input().strip())

   binary_representation = bin(n)[2:]
   ones = re.findall(r"[1]{2,}",binary_representation)

   l = []
   if ones:
      for j in ones:
         l.append(len(j))
      l.sort(reverse=True)
      print(l[0])
   else:
      print(1)
   



