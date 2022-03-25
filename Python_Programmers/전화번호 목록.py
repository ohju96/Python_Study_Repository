def solution(phone_book):

    phone_book.sort()

    answer = True

    phone_length = len(phone_book)

    for i in range(phone_length-1):
        if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
            answer = False
            break
    return answer

print(solution(["119", "97674223", "1195524421"]))