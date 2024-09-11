import  numpy
numpy.set_printoptions(legacy='1.13')
n,m= map(int,input().split(" "))

print(f"{numpy.eye(n,m)}")
