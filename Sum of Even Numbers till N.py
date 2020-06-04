def printSum(x):
    sum = 0
    while x >= 0:
        if x % 2 == 0:
            sum = sum + x
        x = x - 1
    return sum
n = int(input())
x = printSum(n)
print(x)
