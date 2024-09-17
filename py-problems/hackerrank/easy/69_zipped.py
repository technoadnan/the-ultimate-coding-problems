student, sub = map(int, input().split())
marks = [list(map(float, input().split())) for _ in range(sub)]

for j in zip(*marks):
   print(sum(j) / sub)
