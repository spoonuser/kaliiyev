def generator(n):
    while n >= 0:
        yield n
        n -= 1
n = int(input())
x = generator(n)
for a in x:
    print(a)
