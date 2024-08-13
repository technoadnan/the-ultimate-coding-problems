def count_substring(string, sub_string):
   s = len(sub_string)
   c = len(string)
   count = 0
   for i in range(c):
      a = string[i:s]
      print(a)
      if a == sub_string:
         count = count + 1
      s = s + 1
   return count

if __name__ == '__main__':
   string = input().strip()
   sub_string = input().strip()
   
   count = count_substring(string, sub_string)
   print(count)