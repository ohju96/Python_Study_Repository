# 백준 알고리즘 2754번 파이썬 풀이
n = int(input())

if n%4==0 and n%100!=0 or n%400==0:
    print("1")
else:
    print("0")