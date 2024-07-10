import time
if __name__ == '__main__':
   # store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
   
   py_students = [['ha', 37.21], ['r', 37.21],['wrr', 37.2],['ertr', 41],['fdger', 39]]
   # for _ in range(int(input())):
   #    name = input()
   #    score = float(input())
   #    py_students.append([name,score])

   # for j in py_students:
   lowest_score = float('inf') # to find lowest number
   # second_lowest = 
   # for i, k in enumerate(py_students):
   #    if k[1] < lowest_score:
   # #       lowest_score = k[1]
   #       print(k)
   # print(lowest_score)

   # for j in py_students:
   #    print(j)

   all_scores = set()
   for j in range(len(py_students)):
      all_scores.add(py_students[j][1])
   print(sorted(all_scores)[1])

      # if py_students[j][1] < lowest_score:
      #    lowest_score = py_students[j][1]
      # print(py_students[j][1])
      # print(j)

   # print(lowest_score)