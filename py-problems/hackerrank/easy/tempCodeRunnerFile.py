def print_formatted(number):
    # your code goes here
    for j in range(1,number+1):
        # print(j,oct(j).split("0o")[1],hex(j),bin(j),"\n")
        print(hex(j).split("0o")[1])
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)