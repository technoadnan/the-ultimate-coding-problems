def average(array):
    # your code goes here
    # return f"{(sum(array)/len(array)):.3f}" 
    array = set(array) # to remove repetative 
    return f"{sum(array)/len(array):.3f}"

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)