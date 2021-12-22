import sys

def reverse(x):
    # 초기화 하나 한다.
    res=0
    # while 문으로 x가 0보다 클 때 항상 반복문을 돌려준다.
    while x>0:
        # x의 1의 자리 숫자가 t가 된다.
        t=x%10
        res=res*10+t
        # x는 10으로 나눈 몫으로 바꿔진다.
        x=x//10
    # res를 리턴한다.
    return res

def isPrime(x):
    # x의 값이 1일 수 있다.
    if x==1:
        # False 시켜줘야 한다.
        return False
    # 소수를 구하려면 값의 반 정도까지만 구하면 된다.
    # 그 뒤쪽은 어차피 다 걸러진다.
    # 2로 나눈 몫의 +1을 해줘 절반까지 돌게 한다.
    for i in range(2, x//2+1):
        # x는 i의 약수가 존재하면
        if x%i==0:
            # 리턴을 False한다.
            return False
    #위 와 같은 상황이 아니라면
    else:
        # 정상적으로 끝난 값을 True해 준다.
        return True

n=int(input())
a=list(map(int,input().split()))

for x in a:
    # x를 reverse 함수로 보내고 리턴 받아 tmp에 담는다.
     tmp = reverse(x)
    # reverse 된 값을 inPrime, 소수 구하는 함수에 보내 리턴 받아 값을 나타낸다.
     if isPrime(tmp):
         print(tmp, end=" ")
