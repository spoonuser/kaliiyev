import re
s = str(input("Input String :"))
p =re.compile('a+b*')
n = p.search(s)
if n:
    print(s)
else:
    print("Not found")    
     