# 백준 10871번 파이썬 풀이
n, x= map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
    if a[i] < x:
        print(a[i], end=" ")
        # 원래는 세로로 출력이 되는데 end=" "로 세로가 아닌 중간 공백을 넣어 가로로 출력이 되도록 합니다.
