a= set(input().split())
b = int(input())
output = True

for i in range(b):
    s = set(input().split())
    if not s.issubset(a):
        output = False
    if len(s) >= len(a):
        output = False

print(output)
