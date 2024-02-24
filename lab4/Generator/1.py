def generator(n):
    for i in range(n):
        yield i**2
n = int(input())
square = generator(n)         
for j in square:
    print(j)
    
    