
def print_rangoli(size):
    import string
    letters = string.ascii_lowercase[:size]
    lines = []
    for i in range(size):
        s = '-'.join(letters[size-1:i:-1] + letters[i:size])
        lines.append(s.center(4*size - 3, '-'))
    print('\n'.join(lines[::-1] + lines[1:]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)