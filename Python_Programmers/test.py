def solution(participant, completion):

    tmp=0
    dic={}

    for i in participant:
        dic[hash(i)] = i
        tmp += int(hash(i))
    for com in completion:
        tmp -= hash(com)
    return dic[tmp]

print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))