# 백준 알고리즘 2884번 파이썬 풀이
hour, min = map(int, input().split())

if min >= 45:
    print(hour, min - 45)
elif hour > 0 and min < 45:
    print(hour - 1, min + 15)
else:
    print(23, min + 15)