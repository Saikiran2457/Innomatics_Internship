if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
ans = sorted(list(set(arr)))
print(ans[-2])
