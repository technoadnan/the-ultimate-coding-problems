if __name__ == '__main__':
   N = int(input())
   l = []
   for _ in range(N):
      command = input("")
      multiple_cmd = command.split(" ")

      if len(multiple_cmd) > 2:
         c1 = int(multiple_cmd[1])
         c2 = int(multiple_cmd[2])
      elif len(multiple_cmd) > 1:
         c1 = int(multiple_cmd[1])
      
      if multiple_cmd[0] == "insert":
         l.insert(c1, c2)
      elif multiple_cmd[0] == "print":
         print(l)
      elif multiple_cmd[0] == "remove":
         l.remove(c1)
      elif multiple_cmd[0] == "append":
         l.append(c1)
      elif multiple_cmd[0] == "sort":
         l.sort()
      elif multiple_cmd[0] == "pop":
         l.pop()
      elif multiple_cmd[0] == "reverse":
         l.reverse()
