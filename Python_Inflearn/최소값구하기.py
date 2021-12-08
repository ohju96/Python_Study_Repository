arr =[5, 3, 7, 9, 2, 5, 2, 6]
arrMin=float('inf') #최초에는 가장 큰 값이 있다.무한대이다.
for i in range(len(arr)): #arr의 개수 만큼 반복한다.
    if arr[i] < arrMin:# arr[i]가 무한대보다 작을 때, 무조건 처음엔 참이 되도록 위에서 무한대로 설정한다.
#arr에서 앞에 2와 뒤에 2가 있는데 < 부등호를 사용했기 때문에 앞에 2가 들어간다.
#뒤에 2를 사용하기 위해서는 <=를 사용하면 뒤에 값이 들어간다.
        arrMin=arr[i]#arrMin에 arr[i]를 넣는다. 즉, 제일 작은 값이 들어가게 된다.
print(arrMin)
