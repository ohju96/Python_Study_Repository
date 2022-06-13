# t = 테스트 케이스(2)회 출력
t = int(input())

# 테스트 케이스 만큼 실행한다. 2회의 테스트 케이스를 뽑기 위해 2회 실행.
for i in range(t):

    # n = 첫 번째 줄(6)
    # s ~ e = 오름차순정렬대상(2) ~ (5)
    # k = 번째 수 출력(3)
    n, s, e, k = map(int, input().split())

    # n개의 숫자를 받기 위한 list 생성
    a = list(map(int, input().split()))

    # list a의 0번째 인덱스에 첫 번째 값이 들어가 있으므로 s번째는 s-1이 된다.
    a = a[s-1:e]

    # 오름차순정렬을 후 k번째를 출력해야 하므로 sort() 해준다.
    a.sort()

    # 출력 예제에 따라 포멧 형식을 다듬어 알맞게 출력을 해준다.
    print("#%d %d" %(i+1, a[k-1]))