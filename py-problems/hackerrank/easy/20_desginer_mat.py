def print_door_mat(N, M):
    # Top half
    for i in range(1, N, 2):
        pattern = '.|.' * i
        print(pattern.center(M, '-'))
    
    # Center line
    print('WELCOME'.center(M, '-'))
    
    # Bottom half
    for i in range(N-2, 0, -2):
        pattern = '.|.' * i
        print(pattern.center(M, '-'))

# Input values
N, M = map(int, input().split())

# Print the door mat design
print_door_mat(N, M)
