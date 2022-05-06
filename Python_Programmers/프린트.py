from collections import deque

def solution(priorities, location):
    myDeque = deque([v, i] for i, v in enumerate(priorities))
    answer = 0
    idx = 0
    while myDeque:

        idx += 1

        firstData = myDeque.popleft()

        if myDeque and max(myDeque)[0] > firstData[0]:
            myDeque.append(firstData)

        else:
            answer += 1

            if location == firstData[1]:
                break
    return answer


print(solution([2, 1, 3, 2], 2))
# 1

print(solution([1, 1, 9, 1, 1, 1], 0))
# 5