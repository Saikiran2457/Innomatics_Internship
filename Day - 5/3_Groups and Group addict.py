import re
S=input()
a = re.search(r'([A-Za-z0-9])\1+',S)
if a:
    print(a.group(1))
else:
    print(-1)
