#먼저 반복할 테스트 케이스를 입력받습니다.
t = int(input())
#입력 받은 테스트 케이스만큼 반복해 줍니다.
for i in range(t):
    a, b = map(int, input().split())
    print(a+b)