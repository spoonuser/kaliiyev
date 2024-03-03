s = str(input("Input your string:"))
a = True
s = s.lower()
for i in range(len(s)):
    if s[i] != s[-1-i]:
        a = False
        break
print(a)