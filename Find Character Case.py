def printNum(x):
    if 'A' <= x <= 'Z':
        print(1)
    elif 'a' <= x <= 'z':
       	print(0) 
    else:
        print(-1)

char = input()
c = char[0]
printNum(c)
