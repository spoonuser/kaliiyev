import re
s = str(input("Input String :"))
p =re.compile('a+b{2,3}')
n = p.fullmatch(s)
if n:
    print(s)
else:
    print("Not found")    
     