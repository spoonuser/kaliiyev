import math
def generator(b):
    for i in range(b):
        if(i > a):
            yield i**2
a = int(input())
b = int(input())
square = generator(b)         
for j in square:
    print(j)
    
    