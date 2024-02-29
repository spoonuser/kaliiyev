import re
s = str(input("Input string :"))
p = re.sub(r'([a-z])([A-Z])', r'\1 \2' , s)
print(p)