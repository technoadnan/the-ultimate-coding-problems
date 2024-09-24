s,num = int(input("")), map(int, input("").split(" "))
e = any(str(x) == str(x)[::-1] for x in num) and all(x >=0 for x in num)
print(e)

