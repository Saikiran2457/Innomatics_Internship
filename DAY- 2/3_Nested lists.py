if __name__ == '__main__':
    data=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        data.append([name,score])
a = sorted(set([j for i,j in data]))[1]
ans=[i for i,j in data if j==a]
for i in sorted(ans):
    print(i)
