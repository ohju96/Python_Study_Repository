# 백준 알고리즘 14681번 파이썬 풀이
a, b = map(int, input().split())

if a > 0 and b > 0:
    print("1")
elif a < 0 and b > 0:
    print("2")
elif a < 0 and b < 0:
    print("3")
else:
    print("4")