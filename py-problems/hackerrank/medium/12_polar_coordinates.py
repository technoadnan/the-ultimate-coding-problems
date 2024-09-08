import cmath 
n = eval(input())
ans = "\n".join(map(str,cmath.polar(n)))
print(ans)