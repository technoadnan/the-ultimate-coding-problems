n,m = map(int,input().split())
array = list(map(int,input().split()))
liked = set(map(int,input().split()))
disliked = set(map(int,input().split()))

h = 0

for num in array:
   if num in liked:
      h = h + 1
   elif num in disliked:
      h = h - 1

print(h)
