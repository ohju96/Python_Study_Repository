k,n = map(int, input().split())
Line = []
res = 0
lagest = 0

def Count(len):
    cnt = 0
    for x in Line:
        cnt += (x//len)
    return cnt

for i in range(k):
    tmp = int(input())
    Line.append(tmp)
    lagest = max(lagest, tmp)

lt = 1
rt = lagest

while lt<rt:
    mid = (lt+rt)//2
    if Count(mid) >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
