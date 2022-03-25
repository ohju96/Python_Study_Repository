def solution(participant, completion):
    tmp = 0
    dic = {}
    for p in participant:
        dic[hash(p)] = p
        tmp += int(hash(p))
    for com in completion:
        tmp -= hash(com)
    return dic[tmp]

print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))