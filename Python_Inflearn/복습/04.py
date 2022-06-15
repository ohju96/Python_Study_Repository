n = int(input())
a = list(map(float, input().split()))

# round()를 사용해서 소수 첫째 자리에서 반올림한다.
# sum()을 사용해서 평균을 구하기 위해서 값을 더한다..
avg=round(sum(a)/n)

# 비교를 위해서 정수 자료형의 최대값을 min으로 준다.
min = 2147000000

# idx는 인덱스(학생 번호), x에는 리스트에 있는 값(성적)이 들어간다.
for idx, x in enumerate(a):

    # tmp 임시 변수로 abs()함수를 통해 절대값을 구한다. tmp의 값이 가장 작아야 평균에 가장 가까운 값이다.
    tmp=abs(x-avg)

    # tmp가 읽을 최소 값 설정.
    if tmp<min:

        # 작은 값을 유지하기 위해 더 작은 값을 넣는다.
        min=tmp

        # socre에 점수 값도 가지고 있어야 한다. 거리가 같을 떄 답에 대한 값도 출력해야 한다.
        score=x

        #0번 인덱스를 가진 학생의 실제 번호는 1번이다.
        res=idx+1

        # tmp(거리가) 같은 경우에 점수가 큰 학생이 답이 되기 위해 if를 넣는다.
    elif tmp==min:

        # x는 현재 학생의 점수, score는 이전 학생의 점수
        if x>score:

            # 점수가 큰 현재 학생의 점수를 score에 넣어 갱신
            score=x

            #점수가 큰 학생으로 바꾸기 위해 +1
            res=idx+1

# 평균과 학생 번호를 출력
print(avg, res)