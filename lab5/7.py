import re
snake_case = str(input("Input string :"))
p = re.split('_+' , snake_case )
camel_case = p[0] + ''.join(p.capitalize() for p in p[1:]) 
print(camel_case)