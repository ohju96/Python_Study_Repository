# n, m = map(int, input().split())
# a = list(map(int, input().split()))

n = 4
m = 2
a = [3, 4, 2, 1]

a.sort()
lt = 0
rt = n - 1

while lt <= rt:
    mid = (lt + rt) // 2
    if a[mid] == m:
        print(mid + 1)
        break
    elif a[mid] > m:
        rt = mid - 1
    else:
        lt = mid + 1