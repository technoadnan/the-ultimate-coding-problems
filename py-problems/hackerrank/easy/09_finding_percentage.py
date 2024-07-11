if __name__ == '__main__':
   n = int(input())
   student_marks = {}
   for _ in range(n):
      name, *line = input().split()
      scores = list(map(float, line))
      student_marks[name] = scores
   query_name = input()
   query_num = student_marks[query_name]
   percentage = sum(query_num) / len(query_num)
   print(f"{percentage:.2f}")