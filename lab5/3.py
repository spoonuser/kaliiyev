import re
s = str(input("Input String :"))
p =re.compile('[a-z]_+')
n = p.fullmatch(s)
if n:
    print(s)
else:
    print("Not found")    
     