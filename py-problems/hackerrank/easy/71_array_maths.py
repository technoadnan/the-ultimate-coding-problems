import numpy

n,m = input().split()

array = numpy.array([list(map(int, input().split())) for i in range(int(n))])

print(numpy.prod(numpy.sum(array,axis=0)))
