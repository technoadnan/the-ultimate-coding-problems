vowels = ['a','e','i','o','u','y']

n = int(input())
words = input().split(" ")

score = 0
for word in words:
   vowel_point = 0
   for v in word:
      if v in vowels:
            vowel_point += 1
   if vowel_point % 2 == 1:
      score += 1
   else:
      score += 2
print(score)