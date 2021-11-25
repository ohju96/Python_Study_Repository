# 백준 알고리즘 1330번 파이썬 풀이
a, b = map(int, input().split())
if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')