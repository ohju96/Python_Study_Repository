n, k=map(int, input().split())
a=list(map(int, input().split()))

 #set은 중복 제거에 사용합니다.
res=set()
#첫 번째로 값을 뽑습니다.
for i in range(n):
    #두 번째로 값을 뽑습니다.
    for j in range(i+1, n):
        #세 번째로 값을 뽑습니다.
        for m in range(j+1, n):
            #set()으로 만든 res에 값을 담습니다.
            #set은 중복을 제거하기 때문에 같은 값이 여러번 저장되어도 한 번만 담깁니다.
            res.add(a[i]+a[j]+a[m])

#set은 sort가 없기 때문에 정렬을 하려면 list에 담아 정렬을 해야 합니다.
res=list(res)
#list에 담은 res값을 sort로 정렬해 주는데 내림차순 정렬을 위해 reverse값을 True로 줍니다.
res.sort(reverse=True)
print(res[k-1])