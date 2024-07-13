if __name__ == '__main__':
   N = int(input())
   l = []
   for _ in range(N):
      command = input("")
      multiple_cmd = command.split(" ")
      # print(command)
      c1 = int(multiple_cmd[1])
      c2 = int(multiple_cmd[2])
      print(l)
      if command[0] == "insert":
         l.insert(c1, c2)
      elif command == "print":
         print(l)
      elif command == "remove":
         l.remove(c1)
      elif command == "append":
         l.append(c1)
      elif command == "sort":
         l.sort()
      elif command == "pop":
         l.pop()
      elif command == "reverse":
         l.reverse()
