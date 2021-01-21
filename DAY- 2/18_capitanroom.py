a = int(input())
set_b = set()
sumlist_b = 0
for i in input().split():
    I = int(i)
    set_b.add(I)
    sumlist_b += I

print((sum(set_b)*a - sumlist_b)//(a-1))
