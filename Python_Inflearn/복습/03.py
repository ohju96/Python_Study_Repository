n, k = map(int, input().split())
a = list(map(int, input().split()))

# set 자료구조는 중복을 제거한다.
res = set()

# 중복을 방지하면서 뽑기 위해서 마지막 숫자를 돌려주면서 카운팅 뽑아준다.
# a 리스트에 0번 인덱스부터 자료가 들어가서 0부터 for문이 돌아야한다.
for i in range(n):

    # i가 1을 뽑으면 j는 +1을 해서 2를 뽑는다.
    for j in range(i+1, n):

        # j가 2를 뽑으면 m은 +1을 해서 3을 뽑는다.
        for m in range(j+1, n):

            # set은 add로 값을 넣어준다.
            # 위에 for문을 통해 중복을 줄여주면서 값을 담아줄 수 있다.
            res.add(a[i] + a[j] + a[m])

# 리스트에 담아준다.
res = list(res)

# 내림차순 정렬을 위해 reverse를 true로 준다.
res.sort(reverse=True)

# k번째를 뽑아야 하는데 0번 인덱스부터 있기 때문에 -1을 해준다.
print(res[k-1])


