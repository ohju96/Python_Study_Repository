n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

res = 0
s = e = n//2

for i in range(n):
    # j for문은 e까지 돈다.
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(res)