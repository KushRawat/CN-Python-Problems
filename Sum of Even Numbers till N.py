def printSum(x):
    sum = 0
    for i in range(1, x+1):
        if i % 2 == 0:
            sum = sum + i
    return sum

n = int(input())
x = printSum(n)
print(x)
