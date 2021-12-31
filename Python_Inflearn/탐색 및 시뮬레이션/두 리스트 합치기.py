a = input()
n = list(map(int, input().split()))
b = input()
m = list(map(int, input().split()))
c = [] #두 리스트를 합쳐서 받을 리스트이다.
p1 = p2 = 0 #리스트의 인덱스 값을 가르킬 것이다.

while p1 < n and p2 < m:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1

# while문이 둘 중 하나가 완료되어 끝났을 때 나머지 하나를 리스트에 합친다.
if p1 < n:
    c = c+a[p1:]

if p2 < m:
    c = c+b[p2:]

for x in c:
    print(x, end = ' ')
