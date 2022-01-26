def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(x*i)
    return answer;

test = solution(2, 5)
print(test)