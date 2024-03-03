import time
x = int(input("Input your integer: "))
y = int(input("Input time:"))
start = time.time()
time.sleep(y/1000)
if time.time() - start >= y/1000:
    print("Square root of", x ,  "after", y, "miliseconds is",x**0.5)




