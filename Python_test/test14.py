# 완주하지 못한 선수
import collections
def solution0(a, b):
    answer = collections.Counter(a) - collections.Counter(b)
    return list(answer.keys())[0]

# 전화번호목록
def solution1(a):
    a = sorted(a)
    for i, j in zip(a, a[1:]):
        if j.startswith(i):
            return False
    return True

# 위장
def solution2(a):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in a])
    answer = reduce(lambda x,y: x*(y+1), cnt.values(), 1) - 1
    return answer

# K번째 수
def solution3(a, b):
    return list(map(lambda x: sorted(a[x[0]-1:x[1]])[x[2]-1, b]))

# 가장 큰 수
def solution4(a):
    a = list(map(str,a))
    a.sort(key=lambda x: x * 3, reverse=True)
    return str(''.join(a))

# H Index
def solution5(a):
    a.sort(reverse=True)
    answer = max(map(min, enumerate(a, start=1)))
    return answer

# 모의 고사
