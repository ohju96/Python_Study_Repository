# 백준 알고리즘 10430번 파이썬 풀이
a, b, c = map(int, input().split())
print((a+b)%c)
print(((a+c)+(b+c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)