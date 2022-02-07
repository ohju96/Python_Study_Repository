def solution(n):
    aList = list(str(n))
    aList.sort(reverse = True)
    answer = int("".join(aList))
    return answer