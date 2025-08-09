def plusMinus(arr):
    n = len(arr)
    countPos = countNeg = countZero = 0

    for num in arr:
        if num > 0:
            countPos += 1
        elif num < 0:
            countNeg += 1
        else:
            countZero += 1

    posFraction = countPos / n
    negFraction = countNeg / n
    zeroFraction = countZero / n

    print(f"{posFraction:.6f}")
    print(f"{negFraction:.6f}")
    print(f"{zeroFraction:.6f}")


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
