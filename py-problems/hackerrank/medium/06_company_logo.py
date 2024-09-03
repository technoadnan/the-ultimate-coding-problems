from collections import Counter


if __name__ == '__main__':
   s = sorted(input())
   a = Counter(s).most_common(3)
   for k in a:
      print(f"{k[0]} {k[1]}")