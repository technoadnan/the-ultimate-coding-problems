import time
if __name__ == '__main__':
   # store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
   
   py_students = []
   # py_students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
   for _ in range(int(input())):
      name = input()
      score = float(input())
      py_students.append([name,score])

   all_scores = sorted(set([score for name,score in py_students]))
   second_lowest_num = all_scores[1]

   second_lowest_students = sorted([name for name,score in py_students if score == second_lowest_num])

   for name in second_lowest_students:print(name)