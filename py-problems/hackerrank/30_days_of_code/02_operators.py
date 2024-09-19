#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
# meal_cost = float(input())
#  2. INTEGER tip_percent
# tip_percent = int(input())
#  3. INTEGER tax_percent
# tax_percent = int(input())
#

def solve(meal_cost, tip_percent, tax_percent):
   print(round(meal_cost/100 * tip_percent + tax_percent/100 * meal_cost + meal_cost))


if __name__ == '__main__':
   meal_cost = float(input().strip())

   tip_percent = int(input().strip())

   tax_percent = int(input().strip())

   solve(meal_cost, tip_percent, tax_percent)
