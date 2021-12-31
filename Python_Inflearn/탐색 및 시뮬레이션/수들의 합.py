# 입력 받는 변수
n, m = map(int, input().split())
a = list(map(int, input().split()))

# 알고리즘 풀이에 사용 될 전역 변수
lt = 0
rt = 1
tot = a[0]
cnt = 0

# 알고리즘 로직
while True: # while문에 True값을 줘서 무한 반복문을 완성시킨다.
    if tot<m:
        if rt<n:
            tot+=a[rt]
            rt+=1
        else: # 더할 게 없을 경우를 위해 else문에 break를 걸어준다.
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1

print(cnt)