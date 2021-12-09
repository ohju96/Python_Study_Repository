n = int(input())
a = list(map(float, input().split()))
#소수 첫째 자리에서 반올림하기 위해 round()함수를 사용합니다.
#평균을 구하기 위해 값을 다 더해야 하므로 sum()함수를 사용합니다.
avg=round(sum(a)/n)
#정수 자료형의 최대값을 min값으로 줍니다. (비교를 위해서)
min = 2147000000
#임시 변수 idx, x를 만들어 줍니다.
#idx에는 인덱스 값이 들어가고 (학생 번호)
#x에는 리스트에 있는 값이 들어갑니다. (성적)
for idx, x in enumerate(a):
    #tmp라는 임시 변수를 만들어 abs()함수로 절대값을 구해줍니다.
    #평균 점수가 같을 경우 빠른 인덱스 값을 가지고 있는 학생을 출력하기 위해 절대적 거리를 만들어 줍니다.
    #tmp의 값이 가장 작은 값이 평균에 가장 가까운 값입니다.
    tmp=abs(x-avg)
    #tmp가 읽을 최소값을 설정해 줍니다.
    if tmp<min:
        #작은 값을 유지하기 위해 작은 값에 더 작은 값을 넣어줍니다.
        min=tmp
        #score에 점수 값도 가지고 있어야 합니다. 거리가 같을 때 답에 대한 값도 출력해야 하기 때문입니다.
        score=x
        #0번 인덱스를 가진 학생의 실제 번호는 1번입니다.
        res=idx+1
        # 같은 거리일 경우도 계산하기 위해 elif문을 사용해 줍니다.
        # tmp(거리가) 같은 경우에 점수가 큰 학생이 답이 되기 위해 if를 넣어줍니다.
    elif tmp==min:
        # x는 현재 학생의 점수, score는 이전 학생의 점수
        if x>score:
            # 점수가 큰 현재 학생의 점수를 score에 넣어 갱신해 줍니다.
            score=x
            #점수가 큰 학생으로 바꾸기 위해 +1을 합니다.
            res=idx+1
# 평균과 학생 번호를 출력해 줍니다.
print(avg, res)
