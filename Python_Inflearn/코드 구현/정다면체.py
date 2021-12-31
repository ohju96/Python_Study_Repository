# 정다면체
import sys
n, m = map(int, input().split())
# n과 m의 합의 값을 담아둘 리스트를 만들고 크기를 n과 m을 더하고 좀 여유있게 3만큼 추가한 크기를 주었습니다.
cnt = [0]*(n+m+3)
# 정수 자료형 최소값을 넣어줍니다.
max=-2147000000
for i in range(1, n+1):
    for j in range(1, m+1):
        # cnt에 n과m의 합을 인덱스 넘버로 설정하고 값은 합이 같을 때 1씩 증가시켜 줍니다.
        cnt[i+j] += 1
        # 최대 값을 찾기 위해 max에 누적시켜줍니다.
for i in range(n+m+1):
    if cnt[i]>max:
        max=cnt[i]
        # 최대 값이 같은게 여러개 있을 수도 있으니 모두 출력을 위해서 최대값이 같은 n+m의 합을 찾아 출력합니다.
for i in range(n+m+1):
    if cnt[i]==max:
        print(i, end=' ')