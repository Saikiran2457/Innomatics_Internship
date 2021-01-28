T=int(input())
for i in range(T):
    try:
        N=input()
        if len(N)>1:
            N=float(N)
            if N:
                print(True)
        else:
            print(False)
    except:
        print(False)
