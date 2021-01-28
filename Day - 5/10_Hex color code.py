import re

a = re.compile("(#[a-fA-F\d]{6}|#[a-fA-F\d]{3});*")
for i in range(int(input())):
    line = input()
    if line.startswith("#"):
        continue

    for match in re.findall(a,line):
        print(match)
