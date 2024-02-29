import re
camel_case = str(input("Input string :"))
sneak_case = re.sub('([a-zA-Z0-9])([A-Z])',r'\1_\2' , camel_case)
print(sneak_case.lower())
