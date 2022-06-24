s = input()
# 누적을 위한 전역변수
res = 0
for x in s:
    # isdecimal은 0부터 9까지만 찾아준다.
    # isdigit은 제곱까지 다 찾아준다.
    if x.isdecimal():
        res = res*10+int(x)
print(res)
cnt = 0
for i in range(1, res+1):
    if res%i==0:
        cnt += 1
print(cnt)