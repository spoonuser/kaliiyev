s = str(input())
uppercounter = 0
lowercounter = 0
for i in s:
    if i.isupper():
        uppercounter = uppercounter + 1
    elif i.islower():
        lowercounter = lowercounter + 1
        
print("The sum of uppercases:", uppercounter)
print("The sum of lowercases:", lowercounter)