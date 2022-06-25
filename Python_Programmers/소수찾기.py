import math
from itertools import permutations

# 에라토스 테네스의 체
def numberCheck(num):
    if num == 0 or num == 1: # 0,1은 소수가 아님
        return False
    else:
        for i in range(2, int(math.sqrt(num)) + 1): # 입력받은 숫자의 제곱값까지 반복
            if num % i == 0: # 입력 받은 값이 2부터 시작해서 나눠 떨어지는지 체크
                return False
    return True

def solution(numbers):
    answer = []

    for i in range(1, len(numbers) + 1): #숫자 길이만큼 반복
        arr = list(permutations(numbers, i)) # 경우의 수를 순열로 배열
        for j in range(len(arr)): # 모든 경우의 수 반복
            num = int(''.join(map(str,arr[j]))) # 문자를 숫자로 변환 011 -> 11
            if numberCheck(num): #소수인지 확인
                answer.append(num) # 소수면 정답에 저장
    answer = set(answer) # set으로 중복 제거
    return len(answer) # set 구조의 숫자 계산