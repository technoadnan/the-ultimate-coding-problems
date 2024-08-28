n = int(input())
eng_subs = set(map(int, input().split()))
s = int(input())
fr_subs = set(map(int, input().split()))

union_subs = eng_subs.union(fr_subs)

print(len(union_subs))