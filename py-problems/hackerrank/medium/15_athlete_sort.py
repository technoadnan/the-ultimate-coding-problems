

import math
import os
import random
import re
import sys
from operator import itemgetter


if __name__ == '__main__':
   nm = input().split()

   n = int(nm[0])

   m = int(nm[1])

   arr = []

   for _ in range(n):
      arr.append(list(map(int, input().rstrip().split())))

   k = int(input())

   sorted_list = sorted(arr,key=itemgetter(k))

   for j in sorted_list:
      print(" ".join(map(str,j)))
