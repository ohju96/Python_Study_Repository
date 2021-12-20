import sys
n = int(input())
a = list(map(int, input().split()))

def digit_sum(x):
    sum=0
    # str() 함수는 받은 값을 다 쪼개서 문자열로 받는다. 123을 넣으면 1 2 3을 따로 따로 값을 문자열로 가져오는 것이다.
    for i in str(x):
        sum+=int(i)
    return sum

max = -2147000000

# for x in a: 형식으로 작성하면 a리스트에 일일이 접근해 값을 가져온다. 리스트에 1 12 123이 있다면 그대로 1 12 123 따로따로 값을 가져오는 것이다.
for x in a:
    tot=digit_sum(x)
    if tot>max:
        max=tot
        res=x
print(res)