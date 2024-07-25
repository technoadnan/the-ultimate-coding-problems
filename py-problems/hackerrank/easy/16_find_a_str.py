def count_substring(string, sub_string):
   sub = []
   st = []
   for k in range(sub_string):
      sub.append(string[k])
   for j in range(sub):
      st.append(string[j])
   

if __name__ == '__main__':
   string = input().strip()
   sub_string = input().strip()
   
   count = count_substring(string, sub_string)
   print(count)