def avg(x, y, z):
    return (x + y + z) // 3

name = input()
marks = input().split()

m1 = int(marks[0])
m2 = int(marks[1])
m3 = int(marks[2])

print(name)
x = avg(m1, m2, m3)
print(x)
