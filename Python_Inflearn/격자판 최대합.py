n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

# 전역 변수
largest = -2147000000

for i in range(n):
    sum1 = sum2 = 0 #sum1은 행, sum2는 열
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]

    # 가장 큰 경우를 구해야 하니 largest에 큰 값을 계속 갱신해 준다.
    if sum1 > largest:
        largest = sum1

    if sum2 > largest:
        largest = sum2

# 대각선 값 구하기
sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-i-1]

# 마찬가지로 largest에 제일 큰 값을 갱신해 주도록 한다.
if sum1 > largest:
    largest = sum1

if sum2 > largest:
    largest = sum2

print(largest)