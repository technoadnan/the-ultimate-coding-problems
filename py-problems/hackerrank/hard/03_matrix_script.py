import re
first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

single_char = [list(row) for row in zip(*matrix)]
flat_string = ''.join(map(str, [item for sublist in single_char for item in sublist]))

regex = r"(?<=[0-9a-zA-Z])[!,@,#,$,%,&,\s]+(?=[0-9a-zA-Z])"

a = re.sub(regex," ", flat_string)
print(a)
