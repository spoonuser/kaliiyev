def generator(n):
    for i in range(n):
        yield i
n = int(input())
square = generator(n)         
for j in square:
    if(j % 2 == 0):
        print(j)
    