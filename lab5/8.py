import re
s = str(input("Input string :"))
p = re.findall('[A-Z][^A-Z]*' , s)
print(p)