from time import sleep

def merge_the_tools(string, k):
   all_sub_str = []
   # your code goes here
   new_str = ""
   for j in range(len(string)):
      new_str += string[j]

      if (j + 1) % k == 0:
         all_sub_str.append(set(new_str)) 
         new_str = ""
   for j in all_sub_str:
      print(''.join(j))

if __name__ == '__main__':
   string, k = input(), int(input())
   merge_the_tools(string, k)