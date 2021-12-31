import sys
n = int(input())
res = 0
for i in range(n):
    tmp = input().split()
    # tmp를 오름차순 정렬해 준다.
    tmp.sort()
    # tmp가 지금 문자열로 받아졌기 떄문에 int 형으로 변환해서 받아준다.
    a, b, c = map(int, tmp)
    if a == b and b == c:
        # a, b, c 모두 같은 값이라 아무 값이랑 1000이랑 곱해준다.
        money = 10000 + (a * 1000)
    elif a == b or a == c:
        money = 1000 + (a * 100)
    elif b == c:
        money = 1000 + (b * 100)
    else:
        money = c * 100

    if money > res:
        res = money
print(res)
