def solution(n):
    a = list(str(n))
    a.reverse()
    return list(map(int, a))

print(solution(12345))