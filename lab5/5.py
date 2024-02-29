import re
s = str(input("Input String :"))
p =re.compile('a+[a-zA-Z0-9]*b$')
n = p.search(s)
if n:
    print(s)
else:
    print("Not found")    
     