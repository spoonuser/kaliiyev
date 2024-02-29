import re
s = str(input("Input String :"))
p =re.compile('[A-Z]+[a-z]+')
n = p.fullmatch(s)
if n:
    print(s)
else:
    print("Not found")    
     