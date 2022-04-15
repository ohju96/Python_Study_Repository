def solution(answers):

    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    result = {1: 0, 2: 0, 3: 0}

    for i in range(len(answers)):

        if student1[i % 5] == answers[i]:
            result[1] += 1

        if student2[i % 8] == answers[i]:
            result[2] += 1

        if student3[i % 10] == answers[i]:
            result[3] += 1

    top_score = max(result.values())

    answer = []

    for i in range(1, 4):
        if result[i] == top_score:
            answer.append(i)

    return answer