str = input()
r = ''
for i in str: 
    if i.islower():
        r += i.upper()
    else: 
        r += i.lower()
print(r)