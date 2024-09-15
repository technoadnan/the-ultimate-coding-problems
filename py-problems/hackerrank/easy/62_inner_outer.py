import numpy

A = numpy.array(list(map(int,input("").split(" "))))
B = numpy.array(list(map(int,input("").split(" "))))

# print(numpy.inner(A,B),"\n",numpy.outer(A,B))
print(f"{numpy.inner(A,B)}\n{numpy.outer(A,B)}")
