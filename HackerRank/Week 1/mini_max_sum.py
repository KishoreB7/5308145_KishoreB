def miniMaxSum(arr):
    total = sum(arr)
    minimum = min(arr)
    maximum = max(arr)
    print(total - maximum, total - minimum)

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    miniMaxSum(arr)
