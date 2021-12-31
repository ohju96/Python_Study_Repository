n = int(input())
a = list(map(int, input().split()))

# 점수를 합해야 한다.
sum = 0
# 가중치
cnt = 0

# 리스트 a에서 첫 번째 인덱스 값부터 끝까지 하나씩 뺴준다.
for x in a:
    # x가 1이랑 같다면 == 점수가 1점일 때
    if x == 1:
        # 연속으로 정답을 맞추면 1씩 증가된 값을 더해야 하기 때문에 cnt에 가중치를 준다.
        cnt += 1
        # 가중치 값을 sum(합계)에 담아준다.
        sum += cnt
    # x가 1이 아닐 때 == 정답이 아닐 때
    else:
        # 점수 가중치는 없으므로 0을 넣어주고
        cnt = 0
# 다 끝나면 sum(합계)를 출력해준다.
print(sum)