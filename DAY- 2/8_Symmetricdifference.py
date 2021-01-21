m=int(input())
M=set(map(int,input().split()))
n=int(input())
N=set(map(int,input().split()))
S = N.symmetric_difference(M)
for i in sorted(S):
    print(i)
