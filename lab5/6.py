import re
s = str(input("Input String :"))
p = re.sub(r'[ ,.]' , ':' ,s)
print(p)