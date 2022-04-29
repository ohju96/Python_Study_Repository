def solution(brown, yellow):
    answer = []

    ab = brown + yellow

    for b in range(1, ab+1):
        a = ab/ b

        if a >= b:
            if a*2 + b*2 == brown + 4:
                return [a,b]